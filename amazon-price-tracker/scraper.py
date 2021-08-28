import requests
import re
from bs4 import BeautifulSoup


url = "https://www.amazon.co.uk/Sony-ILCE7M3B-Mirrorless-Compact-System/dp/B07B4L1PQ8/?_encoding=UTF" \
      "8&pd_rd_w=PkiU5&pf_rd_p=5772a90e-8b69-4979-9cd5-4e58c7798658&pf_rd_r=N433YXDPH6F0YV8NFW7Z&pd_rd_r" \
      "=9c7c8739-fe8a-450a-8f29-c4e1bed19348&pd_rd_wg=mlfKY&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

headers = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")


def get_product_title():
    return soup.find(id="productTitle").getText().strip()


def get_product_price_str():
    return soup.find(id="priceblock_ourprice").getText().strip().replace(",", "")


def get_product_price_float(price_str):
    return float(re.search(r'[0-9]+', price_str).group())


title = get_product_title()
price_str = get_product_price_str()
price_float = get_product_price_float(price_str)

print(title, " has a price of ", price_str)

if price_float < 1000.00:
    # do something
    pass