#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import models


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        if models.storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(new.name, "")
            self.assertEqual(type(new.name), str)
