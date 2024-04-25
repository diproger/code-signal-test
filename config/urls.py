from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.transactions.views import TransactionListView, TransactionDetailView, TransactionCreateView
from apps.wallets.views import WalletListView, WalletDetailView, WalletCreateView

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="Your project description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('api/transactions/create/', TransactionCreateView.as_view(), name='transaction-create'),

    path('api/wallets/', WalletListView.as_view(), name='wallet-list'),
    path('api/wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('api/wallets/create/', WalletCreateView.as_view(), name='wallet-create'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
