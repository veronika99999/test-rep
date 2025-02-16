class Transport:
"""Базовый класс для автомобилей.
Список атрибутов:
brand (str): марка транспортного средства.
model (str): модель транспортного средства.
year (int): год выпуска.
color (str): цвет.
_mileage (int): пробег"""

    def __init__(self, brand: str, model: str, year: int, color: str, mileage: int = 0) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self._mileage = mileage

    def __str__(self) -> str:
        return f"{self.year} {self.brand} {self.model}, Color: {self.color}, Mileage: {self._mileage}"

    def __repr__(self) -> str:
        return (f"Transport(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"color='{self.color}', mileage={self._mileage})")

    def get_mileage(self) -> int: #возвращение пробега средства
        return self._mileage

    def drive(self, distance: int) -> None:
        if distance > 0:
            self._mileage += distance
        else:
            print("Расстояние должно быть положительным числом.")


class Car(Transport):
"""Дочерний класс для легковых автомобилей.
Список атрибутов:
brand (str): марка автомобиля.
model (str): модель автомобиля.
year (int): год выпуска.
color (str): цвет.
_mileage (int): пробег.
body_type (str): тип кузова
_fuel_level (float): уровень топлива"""

    def __init__(self, brand: str, model: str, year: int, color: str, mileage: int, body_type: str,
                 fuel_level: float = 100.0) -> None:
        super().__init__(brand, model, year, color, mileage)
        self.body_type = body_type
        self._fuel_level = fuel_level

    def __str__(self) -> str:
        return f"{super().__str__()} , Body Type: {self.body_type}, Fuel Level: {self._fuel_level}%"

    def __repr__(self) -> str:
        return (f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"color='{self.color}', mileage={self._mileage}, body_type='{self.body_type}', fuel_level={self._fuel_level})")

    def get_fuel_level(self) -> float: #возвращает текущий уровень топлива
        return self._fuel_level

    def drive(self, distance: int) -> None:
"""Перегрузка метода drive. Увеличивает пробег и уменьшает уровень топлива в зависимости от расстояния.
Перегрузка нужна, потому что у легкового автомобиля, в отличие от базового класса "Транспорт", есть расход топлива."""
        super().drive(distance)  #вызываем метод базового класса для увеличения пробега
        fuel_consumption_rate = 0.1  #расход топлива (литров на километр) - ПРИМЕРНОЕ значение.
        fuel_consumed = distance * fuel_consumption_rate
        self._fuel_level -= fuel_consumed
        if self._fuel_level < 0:
            self._fuel_level = 0.0  # уровень топлива НЕ может быть отрицательным.
        print(f"Потрачено топлива: {fuel_consumed:.2f} л. Остаток топлива: {self._fuel_level:.2f} л.")

    def refuel(self, amount: float) -> None: #заправляет автомобиль
        if amount > 0:
            self._fuel_level += amount
            if self._fuel_level > 100.0:
                self._fuel_level = 100.0  # максимальный уровень - 100%
        else:
            print("Количество топлива для заправки должно быть положительным числом.")