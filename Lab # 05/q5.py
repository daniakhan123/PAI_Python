class Vehicle:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self._price = price
        self.is_available = True
        self.total_rent = 0

    def calculate_rent(self, period):
        self.total_rent = self._price * period
        return self.total_rent

    def display_details(self):
        availability = "Available" if self.is_available else "Not Available"
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Status: {availability}")
        print(f"Total Rental Cost: ${self.total_rent}")

    def rent_vehicle(self, period):
        if self.is_available:
            self.is_available = False
            self.calculate_rent(period)
            print(f"{self.make} {self.model} rented for {period} days.")
        else:
            print(f"{self.make} {self.model} is not available.")

    def return_vehicle(self):
        self.is_available = True
        self.total_rent = 0
        print(f"{self.make} {self.model} returned.")


class Car(Vehicle):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)


class SUV(Vehicle):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)


class Truck(Vehicle):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)


class RentalReservation:
    def __init__(self, vehicle, customer, start_date, end_date):
        self.vehicle = vehicle
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date

    def display(self):
        print(f"Rental Reservation Details:")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Customer: {self.customer.name}")
        self.vehicle.display_details()


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def rent_vehicle(self, vehicle, start_date, end_date):
        period = (end_date - start_date).days
        vehicle.rent_vehicle(period)
        if not vehicle.is_available:
            reservation = RentalReservation(vehicle, self, start_date, end_date)
            self.rental_history.append(reservation)
            return reservation

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print(f"Rental History:")
        for reservation in self.rental_history:
            reservation.display()


if __name__ == "__main__":
    from datetime import datetime, timedelta

    customer = Customer("Dania Khan", "dania@example.com")
    car = Car("Toyota", "Corolla", 30)
    suv = SUV("Honda", "CR-V", 50)
    truck = Truck("Ford", "F-150", 70)

    start_date = datetime.now()
    end_date = start_date + timedelta(days=3)

    reservation = customer.rent_vehicle(car, start_date, end_date)
    customer.display_info()

    car.return_vehicle()
