"""
phone Module

Created on 14.11.2016
@author adiM
"""


def create_phone(manufacturer, model, price):
    """

    :param manufacturer: string with name of manufacturer
    :param model: string with name of model
    :param price: price as an int
    :return:  A phone dictionary
    """
    return {"manufacturer": manufacturer, "model": model, "price": price}


def get_manufacturer(phone):
    """

    :param phone: a phone stored as a dictionary
    :return: the phone manufacturer
    """
    return phone["manufacturer"]


def get_model(phone):
    """

    :param phone: a phone stored as a dictionary
    :return: the phone model
    """
    return phone["model"]


def get_price(phone):
    """

    :param phone: a phone stored as a dictionary
    :return: the pgine price
    """
    return phone["price"]


def set_price(phone, price):
    """

    :param phone: a phone stored as a dictionary
    :param price: the new price as an int
    :return: change the price of one specific phone model with the new price
    """
    phone["price"] = price
