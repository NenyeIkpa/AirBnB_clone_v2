#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import models


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test for state_id """
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        if models.storage_type == 'db':
            self.assertEqual(new.state_id, None)
        else:
            self.assertEqual(new.state_id, "")
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test for name """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        if models.storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(newy.name, "")
            self.assertEqual(type(new.name), str)
