from rest_framework.serializers import ModelSerializer

from homes.models import Home, Country


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = [
            "name"
        ]


class HomesSerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Home
        fields = [
            "street",
            "city",
            "state_zip",
            "country",
            "price",
            "bedrooms",
            "bathrooms",
            "sqft_living",
            "sqft_lot",
            "floors",
            "waterfront",
            "view",
            "condition",
            "sqft_above",
            "sqft_basement",
            "yr_built",
            "yr_renovated",
            "date",
            "created_at",
            "updated_at",
        ]
