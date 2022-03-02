

from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetStores.as_view(), name='get-stores'),
    path('<int:store_id>/orders/', views.AdminGetStoreOrders.as_view(), name='store-orders'),
    path('<int:store_id>/drivers/', views.AdminGetStoreDrivers.as_view(), name='store-orders'),
    path('orders/<int:order_id>/assign/', views.AdminAssignOrderDriver.as_view(), name='store-orders'),
    path('driver/<int:shop_id>/orders/', views.DriverAssignedOrders.as_view(), name='store-orders'),

]
