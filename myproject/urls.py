
from django.contrib import admin
from django.urls import path
from weatherapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('delete/<CName>',views.delete_city,name="DCity")
]
