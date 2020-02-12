from django.urls import include, path
from .views import (
    LoginView, 
    ProfileView, 
    ClientView, 
    ProductView, 
    QuotationView, 
    GroupView, 
    UserView, 
    GeneralView 
    )
# from . import views
from rest_framework import routers
from .models import (
    Product,
    Client
)
from .serializers import (
    ProductSerializer,
    ClientSerializer
)

app_name = 'rutas'
router = routers.SimpleRouter()
router.register(r'login', LoginView)
router.register(r'profile', ProfileView)
router.register(r'user', UserView)
router.register(r'group', GroupView)
router.register(r'client', ClientView)
router.register(r'product', ProductView)
router.register(r'quotation', QuotationView)
urlpatterns = [
    path('example1/', GeneralView.as_view(Model=Product, Serializer=ProductSerializer)),
    path('example2/', GeneralView.as_view(Model=Client, Serializer=ClientSerializer)),
    path(r'', include(router.urls))
]