from dataclasses import field, fields
from rest_framework import serializers
from .models import Order,Store
from user.serializers import DriverSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    driver=DriverSerializer()
    @staticmethod
    def get_order_items(obj):
        if hasattr(obj, "_prefetched_objects_cache") and "order_items" in obj._prefetched_objects_cache:
            return obj._prefetched_objects_cache['order_items'].values_list('item__name','qty', flat=True)
        return obj.order_items.all().values_list('item__name','qty', flat=True)

    class Meta:
        model = Order
        fields = ['id', 'destination', 'order_items',"driver"]


class AdminOrdersSerializer(serializers.ModelSerializer):
    driver=DriverSerializer()
    class Meta:
        model = Order
        fields = ['id', 'destination_long','destination_lat',"driver","status"]

        
class DriverOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=['id', 'destination_long','destination_lat',"status"]



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields=["id","name"]

class OrderDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=["driver"]