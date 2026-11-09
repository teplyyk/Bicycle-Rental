from bike import Bike
from station import Station
from client import Client
from actions import rent_bike, return_bike, admin_report


def main():
    # station_1 = Station("Центр")
    # station_2 = Station("Вокзал")

    bike_1 = Bike(is_electric=True)
    bike_2 = Bike(is_electric=False)

    station_1.add_bike(bike_1)
    station_1.add_bike(bike_2)

    clients = {'roma': 4563,
               'danya': 45}


    #зробити 1 поїздку

    #зробити помилку.


if __name__ == "__main__":
    main()