from .login import UserSerializer
from .profile import ProfileSerializer, UserSerializer, getProfileSerializer
from .client import ClientSerializer
from .product import ProductSerializer, ProductFilter
from .quotation import QuotationSerializer, getQuotationSerializer, QuotationTempSerializer
from .group import GroupSerializer
from .general import GeneralSerializer