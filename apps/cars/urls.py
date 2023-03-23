from django.urls import path

from apps.cars.views import CarViewsCreate,CarGetPutPatchDelete

urlpatterns = [
    path('', CarViewsCreate.as_view(), name='cars_views_create'),
    path('/<int:pk>', CarGetPutPatchDelete.as_view(), name='car_put_putch_delete')
]