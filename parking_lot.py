# parking_lot.py

import random
import string

class ParkingLot:
    def __init__(self, size_sqft, spot_length=8, spot_width=12):
        self.size_sqft = size_sqft
        self.spot_length = spot_length
        self.spot_width = spot_width
        self.num_spots = self.calculate_num_spots()
        self.spots = [None] * self.num_spots  # None means the spot is empty

    def calculate_num_spots(self):
        spot_area = self.spot_length * self.spot_width
        return self.size_sqft // spot_area

    def park_car(self, car, spot_number):
        if spot_number < 0 or spot_number >= len(self.spots):
            return "Invalid spot number. Please choose a valid spot."

        if self.spots[spot_number] is None:
            self.spots[spot_number] = car
            return f"Car with license plate {car.license_plate} parked successfully in spot {spot_number}."
        else:
            return f"Spot {spot_number} is already occupied. Car with license plate {car.license_plate} cannot be parked."

    def is_full(self):
        return all(spot is not None for spot in self.spots)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot):
        if parking_lot.is_full():
            print("Parking lot is full. Cannot park the car.")
            return
        
        # Try to find an empty spot to park the car
        for i, spot in enumerate(parking_lot.spots):
            if spot is None:
                status = parking_lot.park_car(self, i)
                print(status)
                return
