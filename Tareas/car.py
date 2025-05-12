# Estructura Estática
class StaticCar:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    # Getters
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"StaticCar(Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year})"


# Estructura Dinámica
class DynamicCarNode:
    def __init__(self, car=None):
        self.car = car
        self.next = None


class DynamicCarList:
    def __init__(self):
        self.head = None

    def add_car(self, car):
        new_node = DynamicCarNode(car)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_cars(self):
        current = self.head
        while current:
            print(current.car)
            current = current.next


# Ejemplo de uso
if __name__ == "__main__":
    # Estructura Estática
    car1 = StaticCar("Toyota", "Corolla", 2020)
    print(car1)
    car1.set_year(2021)
    print(f"Updated Year: {car1.get_year()}")

    # Estructura Dinámica
    car2 = StaticCar("Honda", "Civic", 2019)
    car3 = StaticCar("Ford", "Focus", 2018)

    car_list = DynamicCarList()
    car_list.add_car(car1)
    car_list.add_car(car2)
    car_list.add_car(car3)

    print("\nDynamic Car List:")
    car_list.display_cars()
