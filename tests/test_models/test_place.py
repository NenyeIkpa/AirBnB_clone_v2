#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))
        if models.storage_type == 'db':
            self.assertEqual(new.city_id, None)
        else:
            self.assertEqual(new.city_id, "")
            self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        if models.storage_type == 'db':
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(new.user_id, "")
            self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        if models.storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(new.name, "")
            self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        if models.storage_type == 'db':
            self.assertEqual(new.description, None)
        else:
            self.assertEqual(new.description, "")
            self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        if models.storage_type == 'db':
            self.assertEqual(new.number_rooms, None)
        else:
            self.assertEqual(type(new.number_rooms), int)
            self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        if models.storage_type == 'db':
            self.assertEqual(new.number_bathrooms, None)
        else:
            self.assertEqual(new.number_bathrooms, 0)
            self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        if models.storage_type == 'db':
            self.assertEqual(new.max_guest, None)
        else:
            self.assertEqual(new.max_guest, 0)
            self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        if models.storage_type == 'db':
            self.assertEqual(new.price_by_night, None)
        else:
            self.assertEqual(new.price_by_night, 0)
            self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        if models.storage_type == 'db':
            self.assertEqual(new.latitude, None)
        else:
            self.assertEqual(new.latitude, 0.0)
            self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))
        if models.storage_type == 'db':
            self.assertEqual(new.longitude, None)
        else:
            self.assertEqual(new.longitude, 0.0)
            self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(models.storage_type == 'db', "skip here")
    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(new.amenity_ids), 0)
