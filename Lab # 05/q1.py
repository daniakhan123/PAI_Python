
class Vehicle:
    capacity = 20
    fare = capacity * 100

    def Printdata(self):
        print("Seating capacityacity: ", self.capacity)
        print("Fare: ", self.fare)


class Bus(Vehicle):
    amount = Vehicle.fare + 10 / 100

    def Printdata(self):
        print("Seating capacityacity: ", Vehicle.capacity)
        print("Total Fare: ", self.amount)


b1 = Bus()
b1.Printdata()
