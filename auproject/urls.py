
from django.contrib import admin
from django.urls import path
from auapp.views import home, usignup, uwelcome, ulogout, urnpassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("usignup/", usignup, name="usignup"),
    path("uwelcome/", uwelcome, name="uwelcome"),
    path("ulogout/", ulogout, name="ulogout"),
    path("urnpassword/", urnpassword, name="urnpassword"),
]
