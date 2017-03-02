"""
test_operations Module

Created on 14.11.2016
@author adiM
"""

from src.domain.operations import add_phone, increase_phone_price, change_all_prices


def test_add_phone():
    l = []
    add_phone(l, "Samsung", "Galaxy", "100")
    add_phone(l, "HTC", "One", "200")
    add_phone(l, "Apple", "iPhone 5", "400")

    assert len(l) == 3

def test_increase_phone_price():
    l = []
    add_phone(l, "Samsung", "Galaxy", "100")
    add_phone(l, "HTC", "One", "200")
    add_phone(l, "Apple", "iPhone 5", "400")

    increase_phone_price(l,"Samsung","Galaxy","300")
    assert l[0]["price"]==400

def test_change_all_prices():
    l = []
    add_phone(l, "Samsung", "Galaxy", "100")
    add_phone(l, "HTC", "One", "200")
    add_phone(l, "Apple", "iPhone 5", "400")

    change_all_prices(l, 10)
    assert l[0]["price"]==110
    assert l[1]["price"]==220
    assert l[2]["price"]==440

def test_operations_all():
    test_add_phone()
    test_increase_phone_price()
    test_change_all_prices()