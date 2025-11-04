#!/usr/bin/env python3

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

class Dog:
    def __init__(self, name = "Pup", breed = "Mastiff"):
      self.name = name
      self.breed = breed

    def get_name(self) :
       return self._name

    def get_breed(self) :
       return self._breed


    def data_type(self, name):
       if((type(name) == str)and (1<= len(name) <=25)):
          self._name = name
       else:
             print("Name must be string between 1 and 25 characters.")

    name = property(get_name, data_type)

    def validity_of_breed(self,breed):
       if breed in APPROVED_BREEDS:
          self._breed = breed
       else:
          print("Breed must be in list of approved breeds.")

    breed = property(get_breed, validity_of_breed)


fido = Dog(name="Fido")
fido.data_type("Fido")
fido.validity_of_breed("Chihuahua")


