"""
ui Module

Created on 14.11.2016
@author adiM
"""

from domain.operations import add_phone, increase_phone_price, change_all_prices
from domain.phone import get_manufacturer, get_model, get_price


def print_menu():
    print("Enter command:")
    print("1 - Add phone")
    print("2 - Print all phones")
    print("3 - Print phones from a given manufacturer")
    print("4 - Increase price of a phone model")
    print("5 - Increase all prices with a given percentage")
    print("x - Exit program\n")


def run_app():
    store = [{"manufacturer": "Samsung", "model": "Note 5", "price": 300},
             {"manufacturer": "HTC", "model": "Desire", "price": 280},
             {"manufacturer": "Apple", "model": "iPhone 5S", "price": 600}]
    options = {"1": ui_add_phone, "2": ui_print_all, "3": ui_print_manufacturer, "4": ui_increase_phone_price,
               "5":ui_change_all_prices}
    while True:
        print("")
        print_menu()
        option = input("Enter option:")
        if option == "x":
            break
        try:
            options[option](store)
        except KeyError:
            print("Option not implemented")
        except ValueError:
            print("Incorrect data")
        except Exception as ex:
            print("An error occured:", ex)
            print("Try again")


def ui_add_phone(store):
    manufacturer = input("Manufacturer: ")
    model = input("Model: ")
    price = input("Price: ")
    try:
        add_phone(store, manufacturer, model, price)
    except ValueError:
        print("Incorrect value. Try again")


def ui_print_phone(phone):
    print("\t Manufacturer: {0} || Model: {1} || Price: {2}".format(get_manufacturer(phone), get_model(phone),
                                                                    get_price(phone)))


def ui_print_all(store):
    print("Phones available in the store:")
    for ph in store:
        ui_print_phone(ph)


def ui_print_manufacturer(store):
    manufacturer = input("Choose a manufacturer:")
    found = False
    for ph in store:
        if get_manufacturer(ph) == manufacturer:
            ui_print_phone(ph)
            found = True
    if not found:
        print("No phones from this manufacturer.")


def ui_increase_phone_price(store):
    manufacturer = input("Manufacturer: ")
    model = input("Model: ")
    price = input("Price: ")
    try:
        increase_phone_price(store, manufacturer, model, price)
    except ValueError:
        print("Incorrect value. Try again")
    except Exception as ex:
        print("Error occurred: ", ex)

def ui_change_all_prices(store):
    try:
        percentage = int(input("Enter percentage: "))
        if percentage in range(-50,100+1):
            change_all_prices(store, percentage)
        else:
            print("Percentage must be between -50 and 100")
    except ValueError:
        print("Invalid input.")