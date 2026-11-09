from bikes import Bike

class Station:
  def __init__(self, name_station: str):
    self.name_station = name_station
    self.bikes: list[Bike] = []
    
  def add_bike(self, bike: Bike) -> None:
    self.bikes.append(bike)

  def remove_bike(self, is_electric: bool) -> Bike | None:
    for bike in self.bikes:
      if bike.is_electric == is_electric:
        self.bikes.remove(bike)
        return bike
    return None
