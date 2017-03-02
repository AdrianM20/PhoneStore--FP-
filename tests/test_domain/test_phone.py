"""
test_phone Module

Created on 14.11.2016
@author adiM
"""

from src.domain.phone import create_phone, get_manufacturer,get_model,get_price,set_price

def test_create_phone():
    phone = create_phone("Samsung", "Galaxy J5", 200)

    assert phone == {"manufacturer":"Samsung", "model":"Galaxy J5","price":200}

def test_get_manufacturer():
    phone = create_phone("Samsung", "Galaxy J5", 200)

    assert get_manufacturer(phone)=="Samsung"

def test_get_model():
    phone = create_phone("Samsung", "Galaxy J5", 200)

    assert get_model(phone) == "Galaxy J5"

def test_get_price():
    phone = create_phone("Samsung", "Galaxy J5", 200)

    assert get_price(phone)==200

def test_set_price():
    phone = create_phone("Samsung", "Galaxy J5", 200)
    set_price(phone, 400)

    assert get_price(phone)==400

def test_phone_all():
    test_create_phone()
    test_get_manufacturer()
    test_get_price()
    test_get_model()
    test_set_price()