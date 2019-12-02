from django.urls import include, path
from .views import LoginView, ProfileView, ClientView, ProductView, QuotationView, GroupView, UserView
from rest_framework import routers

app_name = 'rutas'
router = routers.DefaultRouter()
router.register(r'login', LoginView)
router.register(r'profile', ProfileView)
router.register(r'user', UserView)
router. register(r'group', GroupView)
router.register(r'client', ClientView)
router.register(r'product', ProductView)
router.register(r'quotation', QuotationView)

urlpatterns = [
    path(r'', include(router.urls))
]