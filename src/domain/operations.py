"""
operations Module

Created on 14.11.2016
@author adiM
"""

from domain.phone import create_phone, get_manufacturer, get_model, get_price, set_price


def validator(manufacturer, model, price):
    """

    :param manufacturer: string with name of manufacturer
    :param model: string with name of model
    :param price: price as an string
    :return: Validates if the given values are longer than 2 characters
    """
    if len(manufacturer) < 3:
        raise Exception("Manufacturer name should be at least 3 characters")
    if len(model) < 3:
        raise Exception("Phone model should be at least 3 characters")
    if len(price) < 3:
        raise Exception("Phone price should be at least 3 digits")


def add_phone(store, manufacturer, model, price):
    validator(manufacturer, model, price)
    phone = create_phone(manufacturer, model, int(price))
    store.append(phone)


def increase_phone_price(store, manufacturer, model, price):
    found = False
    for ph in store:
        if get_manufacturer(ph) == manufacturer:
            if get_model(ph) == model:
                new_price = get_price(ph) + int(price)
                set_price(ph, new_price)
                found = True
    if not found:
        raise Exception("Phone not registered yet. No price updated.")


def change_all_prices(store, percentage):
    for ph in store:
        new_price = get_price(ph) + (percentage / 100) * get_price(ph)
        new_price = int(new_price)
        set_price(ph, new_price)
