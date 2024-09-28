class BMW:
    def display_info(self):
        return "This is a BMW. Driving experience: Luxurious and Smooth."
class Ferrari:
    def display_info(self):
        return "This is a Ferrari. Driving experience: Fast and Thrilling."
def car_info(car):
    print(car.display_info())
bmw_car = BMW()
ferrari_car = Ferrari()

car_info(bmw_car)
car_info(ferrari_car)