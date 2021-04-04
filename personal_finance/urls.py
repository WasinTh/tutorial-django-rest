from django.contrib import admin
from django.urls import path
from account.views import current_balance_view, transaction_list_view, TransactionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/current-balance/', current_balance_view),
    path('account/transaction-list/', transaction_list_view),
    path('account/transaction/', TransactionView.as_view()),
]
