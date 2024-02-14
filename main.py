from abc import abstractmethod


#базовый класс машины типа купе
#общая причина инкапусяции атритубов: считаю что так более логично, исключение: состояние дверей
class CoupeCar:
    def __init__(self):
        self._number_of_doors = 2
        self.are_doors_open = False

    #метод для переопределения
    @abstractmethod
    def drive(self) -> None:
        pass

    #метод для наследования
    def check_door(self):
        if self.are_doors_open:
            print("Doors are open, be careful")
        else:
            print("Doors are closed, nothing to worry about")

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__}: {self.__class__.__name__}'


#базовый класс для машины типа седан, по методам все аналогично
class SedanCar:
    def __init__(self):
        self._number_of_doors = 4
        self.are_doors_open = False

    def check_door(self):
        if self.are_doors_open:
            print("Doors are open, be careful")
        else:
            print("Doors are closed, nothing to worry about")

    @abstractmethod
    def drive(self) -> None:
        pass

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__}: {self.__class__.__name__}'


#абстрактая фабрика автомобилей, я считаю, что данный паттерн подходит для задачи
#решил его использовать ради тренировки
class AbstractCarFactory:

    #абстрактные методы создания объектов
    @abstractmethod
    def create_coupe_car(self, car_model: str) -> CoupeCar:
        pass

    @abstractmethod
    def create_sedan_car(self, car_model: str) -> SedanCar:
        pass


#далее идут непосредственные реализации базовых классов
class ToyotaCoupeCar(CoupeCar):

    def __init__(self, car_model: str):
        CoupeCar.__init__(self)
        self._car_make = "Toyota"
        self._car_model = car_model

    def drive(self) -> None:
        print("Driving TOYOTA COUPE CAR")


class ToyotaSedanCar(SedanCar):

    def __init__(self, car_model: str):
        SedanCar.__init__(self)
        self._car_make = "Toyota"
        self._car_model = car_model

    def drive(self) -> None:
        print("Driving TOYOTA SEDAN CAR")


class LadaCoupeCar(CoupeCar):

    def __init__(self, car_model: str):
        CoupeCar.__init__(self)
        self._carMake = "Lada"
        self._carModel = car_model

    def drive(self) -> None:
        print("Driving LADA COUPE CAR")


class LadaSedanCar(SedanCar):

    def __init__(self, car_model: str):
        SedanCar.__init__(self)
        self._carMake = "Lada"
        self._carModel = car_model

    def drive(self) -> None:
        print("Driving LADA SEDAN CAR")


#далее идут непосредственные реализации фабрик для toyota и для lada
#и реализация создания объектов определенных классов
class ToyotaFactory(AbstractCarFactory):

    def create_coupe_car(self, car_model: str) -> CoupeCar:
        return ToyotaCoupeCar(car_model)

    def create_sedan_car(self, car_model: str) -> SedanCar:
        return ToyotaSedanCar(car_model)


class LadaFactory(AbstractCarFactory):

    def create_coupe_car(self, car_model: str) -> CoupeCar:
        return LadaCoupeCar(car_model)

    def create_sedan_car(self, car_model: str) -> SedanCar:
        return LadaSedanCar(car_model)


if __name__ == "__main__":
    lada_factory = LadaFactory()
    lada_sedan = lada_factory.create_sedan_car("priora")
    lada_sedan.check_door()
    lada_sedan.drive()
    lada_coupe = lada_factory.create_coupe_car("2112")
    lada_coupe.check_door()
    lada_coupe.drive()
