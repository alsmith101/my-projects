import pytest
import bitcoin_notifications
from datetime import datetime


def test_format_bitcoin_price_history():
    timestamp = datetime.strptime("2021-07-31 12:00:00", "%Y-%m-%d %H:%M:%S")
    bitcoin_price_history = [
        {"price": 1.0, "timestamp": timestamp},
        {"price": 1.1, "timestamp": timestamp},
        {"price": 1.2, "timestamp": timestamp},
        {"price": 1.3, "timestamp": timestamp},
        {"price": 1.4, "timestamp": timestamp},
    ]
    output = bitcoin_notifications.format_bitcoin_price_history(bitcoin_price_history)
    expected = "2021-07-31 12:00:00: 1.0<br>" \
        "2021-07-31 12:00:00: 1.1<br>" \
        "2021-07-31 12:00:00: 1.2<br>" \
        "2021-07-31 12:00:00: 1.3<br>" \
        "2021-07-31 12:00:00: 1.4"

    assert output == expected