import requests
from bs4 import BeautifulSoup
import argparse

headers = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
}


def scrape_indeed(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.findAll("td", {"class": "resultContent"})


def get_job_title(result):
    job_title = result.find("h2", {"class": "jobTitle jobTitle-color-purple"})
    if job_title:
        return job_title.getText().strip()
    else:
        return None


def get_company_name(result):
    string = ""
    company_names = result.findAll("a", attrs={"data-tn-element": "companyName"})

    if len(company_names) == 0:
        company_names = result.findAll("span", {"class": "companyName"})

    for name in company_names:
        string += name.text.strip()

    return string


def main(url):
    results = scrape_indeed(url)
    jobs = []
    for r in results:
        jobs.append(
            {
                "job-title": get_job_title(r),
                "company-name": get_company_name(r),
             }
        )

    print(jobs)


if __name__ == "__main__":

    base_url = "https://uk.indeed.com"

    parser = argparse.ArgumentParser(description="parse in keywords to search the Indeed website")
    parser.add_argument("keywords", nargs="*", default=[])
    parser.add_argument("--location", default="London")
    args = parser.parse_args()

    keywords = "+".join(args.keywords)
    location = args.location
    url = f"{base_url}/jobs?q={keywords}&l={location}"

    main(url)
