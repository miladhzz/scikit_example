from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import StandarizeView, CustomTokenObtainPairView

urlpatterns = [
    path('standarize', StandarizeView.as_view(), name='standarize'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
