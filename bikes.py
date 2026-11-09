class Bike:
    def __init__(self, number: str, is_electric: bool):
        self.number = number
        self.is_electric = is_electric

    def get_number(self) -> str:
        return self.number

    def get_is_electric(self) -> bool:
        return self.is_electric