# main.py

from parking_lot import ParkingLot, Car
import random
import string

def generate_license_plate():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

def main():
    # Example parking lot creation
    parking_lot = ParkingLot(size_sqft=2000)

    # Generate some cars with random license plates
    num_cars = 20
    cars = [Car(generate_license_plate()) for _ in range(num_cars)]

    # Attempt to park each car
    for car in cars:
        car.park(parking_lot)
        if parking_lot.is_full():
            print("Parking lot is now full. No more cars can be parked.")
            break

if __name__ == "__main__":
    main()
