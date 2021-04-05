from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.routers import DefaultRouter
from account.views import current_balance_view, transaction_list_view, TransactionView, CustomerView, \
    TransactionViewSet, CustomerViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Personal Finance API",
        default_version='v1',
        description="bla bla..",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('account/transaction-viewsets', TransactionViewSet)
router.register('account/customer-viewsets', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('account/current-balance/', current_balance_view),
    path('account/transaction-list/', transaction_list_view),
    path('account/transaction/', TransactionView.as_view()),
    path('account/customer/', CustomerView.as_view()),
]
