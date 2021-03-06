"""
CP1404 Prac_06
Car Class
Benjamin Nicholson
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel = {}, odometer = {}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance


class Limo:
    """Represents a limo instance"""

    def __init__(self, name="", fuel=100):
        """Initialise a Car instance.

         fuel: float, one unit of fuel drives one kilometre
         """
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def add_fuel(self, amount):
        """Adds amount to cars fuel"""
        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance



