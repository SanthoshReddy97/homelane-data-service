from homes.models import Home
from homes.serializers import HomesSerializer


class HomesHandler:

    def __init__(self, request_body):
        self.request_body = request_body
        self.homes = ""

    def method_not_declared(self):
        print(
            f"Operation not defined {self.request_body.get('operation_name')}"
        )

    def get_home_data(self):
        operation_name = self.request_body.get("operation_name")
        method = getattr(self, operation_name, "method_not_declared")
        method()
        return self.serializer_data()

    def price(self):
        max_price = float(self.request_body.get("max_price"))
        min_price = float(self.request_body.get("min_price"))
        self.homes = Home.objects.filter(price__gte=min_price, price__lte=max_price)

    def sqft(self):
        sqft_living = int(self.request_body.get("sqft_living"))
        self.homes = Home.objects.filter(sqft_living__gt=sqft_living)

    def year(self):
        year = int(self.request_body.get("year"))
        self.homes = Home.objects.filter(yr_built__gt=year, yr_renovated__lt=year)

    def serializer_data(self):
        return HomesSerializer(self.homes, many=True).data


def standard_price_calculation():
    homes = Home.objects.all()
    for home in homes:
        price = (((home.bedrooms * home.bathrooms * (
                    home.sqft_living / home.sqft_lot) * home.floors + home.waterfront + home.view) * home.condition * (
                                   home.sqft_above + home.sqft_basement) - 10 * (
                                   2022 - max(home.yr_built, home.yr_renovated)))) * 100
        home.price = "{:.1f}".format(price)
    return HomesSerializer(homes, many=True).data
