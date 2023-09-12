# create a car class

class carRentals:
    def __init__(self,model,make,price,color,year):
        self.Model = model
        self.Make = make
        self.Price = price
        self.Color = color
        self.Year = year


    def rentCar(self,rentee,date):
        print("\t\t\t____Rent Details____")
        print(f"Car Model: {self.Model}")
        print(f"Car Make: {self.Make}")
        print(f"Car Price: {self.Price}")
        print(f"Car Rentee: {rentee}")


# create an instance of car rentals
firstCar = carRentals("Hunda","Accord",50000.45,"Black","2018")

# rent car
firstCar.rentCar(input("Rentee Name:"),input("Date(DD/MM/YY): "))