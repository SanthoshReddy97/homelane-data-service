from django.db import models

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Home(models.Model):

    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state_zip = models.CharField(max_length=15)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name="home_country",
        blank=True,
        null=True
    )
    price = models.FloatField(default=0)
    bedrooms = models.FloatField(default=0)
    bathrooms = models.FloatField(default=0)
    sqft_living = models.IntegerField(default=0)
    sqft_lot = models.IntegerField(default=0)
    floors = models.FloatField(default=0)
    waterfront = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    condition = models.IntegerField(default=0)
    sqft_above = models.IntegerField(default=0)
    sqft_basement = models.IntegerField(default=0)
    yr_built = models.IntegerField(default=0)
    yr_renovated = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street
