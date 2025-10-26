from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, login_view, logout_view

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')), 
    path('login/', login_view),
    path('logout/', logout_view),
]
