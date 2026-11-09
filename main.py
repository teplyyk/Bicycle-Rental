from bike import Bike
from station import Station
from client import Client
from actions import rent_bike, return_bike


def main():
    # Створюємо станції, велосипеди й клієнтів
    center = Station("Центр")
    station_2 = Station("Вокзал")


    center.add_bike(Bike("E-01", True)) #true = електро
    center.add_bike(Bike("B-01", False))

    roma = Client("Roma", 4563)
    danya = Client("Danya", 45)


    print("Звіт адміністратора")
    print(f"Станція {center.name_station}: {len(center.bikes)} велосипед(и)")
    print(f"Станція {station_2.name_station}: {len(station_2.bikes)} велосипед(и)")
    # print(f"Виручка: {total_revenue}")


if __name__ == "__main__":
    main()
