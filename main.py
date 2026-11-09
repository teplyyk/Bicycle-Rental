from bikes import Bike
from cluent import Client
from station import Station
from actions import rent_bike, return_bike, admin_report


def main():
    total_revenue = 0


    center = Station("Центр")
    park = Station("Парк")

    center.add_bike(Bike("E-01", True))
    center.add_bike(Bike("B-01", False))
    park.add_bike(Bike("E-02", True))

    roma = Client("Roma", 4563)
    danya = Client("Danya", 45)

    bike = center.remove_bike(is_electric=True)

    if bike is None:
        print("електрика фолс")
    else:
        cost = 10 * bike.get_bike_cost()

        if roma.charge(cost):
            park.add_bike(bike)
            total_revenue += cost
            print('все добре')

        else:
            center.add_bike(bike)
            print("Не вдалося оплатити поїздку: недостатньо коштів.")

    print('звіт',total_revenue)


if __name__ == "__main__":
    main()