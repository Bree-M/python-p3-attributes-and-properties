#!/usr/bin/env python3

class Dog:

    APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

    def __init__(self, name="Mimi", breed="Corgi"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return getattr(self, "_name", None)

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    @property
    def breed(self):
        return getattr(self, "_breed", None)

    @breed.setter
    def breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None
