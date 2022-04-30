from django.urls import re_path as url

from homes.views import HomesViewset

home_url_patterns = [
    url("homes", HomesViewset.as_view())
]
