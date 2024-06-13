class Vehicle:
    def __init__(self, reg_num):
        self.reg_num = reg_num

    def get_vehicle_type(self):
        return "Generic Vehicle"

    def get_fee(self):
        return 0


class Car(Vehicle):
    def get_vehicle_type(self):
        return "Car"

    def get_fee(self):
        return 500


class Motorcycle(Vehicle):
    def get_vehicle_type(self):
        return "Motorcycle"

    def get_fee(self):
        return 200


class Truck(Vehicle):
    def get_vehicle_type(self):
        return "Truck"

    def get_fee(self):
        return 1500


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity
        self.occupied_spaces = 0
        self.parking_slots = {}

    def park(self, vehicle):
        if self.available_spaces > 0:
            slot = self.find_empty_slot()
            self.parking_slots[slot] = vehicle
            self.available_spaces -= 1
            self.occupied_spaces += 1
            print(f"Vehicle {vehicle.reg_num} ({vehicle.get_vehicle_type()}) parked at slot {slot}")
            self.charge_fee(vehicle)
        else:
            print("Parking lot is full!")

    def find_empty_slot(self):
        for i in range(1, self.capacity + 1):
            if i not in self.parking_slots:
                return i

    def leave(self, slot):
        if slot in self.parking_slots:
            vehicle = self.parking_slots[slot]
            del self.parking_slots[slot]
            self.available_spaces += 1
            self.occupied_spaces -= 1
            print(f"Vehicle {vehicle.reg_num} left from slot {slot}")
        else:
            print("Slot is already empty!")

    def display_status(self):
        print(f"Available Spaces: {self.available_spaces}")
        print(f"Occupied Spaces: {self.occupied_spaces}")
        print("Parking Slots:")
        for slot, vehicle in self.parking_slots.items():
            print(f"Slot {slot}: {vehicle.reg_num} ({vehicle.get_vehicle_type()})")

    def charge_fee(self, vehicle):
        fee = vehicle.get_fee()
        print(f"Charged Tk {fee} for parking {vehicle.get_vehicle_type()}.")


if __name__ == "__main__":
    parking_lot = ParkingLot(100)  # Capacity of 100

    car1 = Car("Dhaka Metro-1123")
    car2 = Car("Dhaka Metro-1207")
    bike = Motorcycle("Khulna-789")
    truck1 = Truck("Dhaka Metro-7101")
    truck2 =Truck("Khulna Kho-1201")

    parking_lot.park(car1)
    parking_lot.park(car2)
    parking_lot.park(bike)
    parking_lot.display_status()
    parking_lot.leave(2)
    parking_lot.display_status()
    parking_lot.park(truck1)
    parking_lot.park(truck2)
    parking_lot.display_status()