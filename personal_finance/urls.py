from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.routers import DefaultRouter
from account.views import current_balance_view, transaction_list_view, TransactionView, CustomerView, \
    TransactionViewSet, CustomerViewSet

router = DefaultRouter()
router.register('account/transaction-viewsets', TransactionViewSet)
router.register('account/customer-viewsets', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('account/current-balance/', current_balance_view),
    path('account/transaction-list/', transaction_list_view),
    path('account/transaction/', TransactionView.as_view()),
    path('account/customer/', CustomerView.as_view()),
]
