from django.urls import path
from account.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
