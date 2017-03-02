"""
test_main Module

Created on 14.11.2016
@author adiM
"""


from test_domain.test_phone import test_phone_all
from test_domain.test_operations import test_operations_all
if __name__ == "__main__":
    test_phone_all()
    test_operations_all()