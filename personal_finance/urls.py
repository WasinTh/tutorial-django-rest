from django.contrib import admin
from django.urls import path
from account.views import current_balance_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/current-balance/', current_balance_view)
]
