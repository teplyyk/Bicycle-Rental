class Bike:
    def __init__(self, number: str, is_electric: bool):
        """Зберігає номер велосипеду і його тип"""
        self.number = number
        self.is_electric = is_electric

    def get_number(self) -> str:
        """Повертає номер велосипеду"""
        return self.number

    def get_is_electric(self) -> bool:
        """Повертає тип велосипеду"""
        return self.is_electric

    def get_bike_cost(self) -> int:
        """Обчислює вартість однієї хвилини на велосипеді та повертає її"""
        if self.is_electric:
            price_per_minute = 5
        else:
            price_per_minute = 2
        return price_per_minute