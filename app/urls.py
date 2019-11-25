from django.urls import include, path
from .views import ProfileView, ClientView, ProductView, QuotationView, GroupView, UserView
from rest_framework import routers

app_name = 'rutas'
router = routers.DefaultRouter()
router.register(r'profile', ProfileView, 'Crud')
router.register(r'user', UserView)
router. register(r'group', GroupView)
router.register(r'client', ClientView)
router.register(r'product', ProductView)
router.register(r'quotation', QuotationView)

urlpatterns = [
    path(r'', include(router.urls))
]