from django.conf.urls import url
from rest_framework import routers
from .views import FlipVendorCrud,FlipProductsCrud,FlipVendorRead


router = routers.DefaultRouter()
#router.register(r'v2', FlipVendorCrud)
router.register(r'v1', FlipVendorRead)
router.register(r'products', FlipProductsCrud)

urlpatterns = router.urls

'''
urlpatterns = [
    path('',include(router.urls))
]
'''