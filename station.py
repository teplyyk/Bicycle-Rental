class Station:
  def __init__(self, name_station):
    self.name_station = name_station
        self.bikes = []
    
  def add_bike(self, bike: Bike):
    self.bikes.append(bike)

  def remove_bike(self, is_electric):
    for bike in self.bikes:
      if bike.is_electric == is_electric:
        self.bikes.remove(bike)
        return bike
    return None
