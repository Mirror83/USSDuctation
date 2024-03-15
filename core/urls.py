
from django.contrib import admin
from django.urls import path
from app.views import UssdCallback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ussd/', UssdCallback.as_view(), name='ussd-callback'),
]
