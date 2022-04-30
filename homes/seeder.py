import csv
from homes.models import Home, Country
from datetime import datetime

country = Country.objects.get(name="USA")
print(country)


def add_homes():
    file = open("/Users/santhoshreddy/homeline_bot/data_service/home_data.csv")
    csvreader = csv.reader(file)
    for index, row in enumerate(csvreader):
        if index == 0:
            continue
        Home.objects.create(
            date=datetime.fromisoformat(row[0]),
            price=float(row[1]),
            bedrooms=float(row[2]),
            bathrooms=float(row[3]),
            sqft_living=int(row[4]),
            sqft_lot=int(row[5]),
            floors=float(row[6]),
            waterfront=int(row[7]),
            view=int(row[8]),
            condition=int(row[9]),
            sqft_above=int(row[10]),
            sqft_basement=int(row[11]),
            yr_built=int(row[12]),
            yr_renovated=int(row[13]),
            street=row[14],
            city=row[15],
            state_zip=row[16],
            country=country,
        )
