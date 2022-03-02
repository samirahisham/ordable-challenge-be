
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from .models import Order,Store
from user.models import StoreDriver
from rest_framework import  status
from rest_framework.response import Response
from .serializers import DriverOrderSerializer,AdminOrdersSerializer,StoreSerializer,OrderDriverSerializer
from user.serializers import DriverSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
import json

class GetStores(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        stores = Store.objects.filter(Q(merchants__merchant__user=request.user )|Q(drivers__driver=request.user )).distinct()
        store_serialized=StoreSerializer(stores,many=True)
        return Response(store_serialized.data)

class AdminGetStoreOrders(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        store_id = kwargs.get("store_id")
        try:
            assigned_filter=request.query_params.get('assigned')
            assigned_filter=not json.loads(assigned_filter.lower())
        except Exception as e:
            assigned_filter=False    
        try:
            store=Store.objects.get(Q(merchants__merchant__user=request.user )|Q(drivers__driver=request.user ),id=store_id)
        except Exception as e:
            return Response("invalid store")
        orders=Order.objects.filter(items__item__store=store,driver__isnull=assigned_filter,status='1')
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginate_by_param = 'page'
        result_page = paginator.paginate_queryset(orders, request)
        serializer = AdminOrdersSerializer(result_page, many=True)
        return (paginator.get_paginated_response(serializer.data))



class AdminGetStoreDrivers(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        store_id = kwargs.get("store_id")
        try:
            store=Store.objects.get(id=store_id,merchants__merchant__user=request.user)
        except Exception as e:
            return Response("invalid store",status=status.HTTP_404_NOT_FOUND)
        drivers=StoreDriver.objects.filter(store=store)
        serializer=DriverSerializer(drivers,many=True)
        return Response(serializer.data)

class AdminAssignOrderDriver(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,*args, **kwargs):
        order_id = kwargs.get("order_id")
        try:
            order=Order.objects.get(id=order_id,items__item__store__merchants__merchant__user=request.user)
        except Exception as e:
            return Response("invalid store",status=status.HTTP_404_NOT_FOUND)
        try:
            employee_id=request.data["employee_id"]
            driver=StoreDriver.objects.get(employee_id=employee_id,store__in=list(order.items.values_list("item__store",flat=True)))
        except Exception as e:
            return Response("invalid store driver",status=status.HTTP_404_NOT_FOUND)
        try:
            order.driver=driver
            order.save()       
        except Exception as e:
            return Response("an error has occured",status=status.HTTP_400_BAD_REQUEST)
        
        order=Order.objects.get(id=order_id,items__item__store__merchants__merchant__user=request.user)
        order.save()
        order.driver.save()
        serializer=OrderDriverSerializer(order)
        return Response(serializer.data)


class DriverAssignedOrders(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        try:
            driver=StoreDriver.objects.get(driver=request.user)
        except Exception as e:
            return Response("invalid store",status=status.HTTP_404_NOT_FOUND)
        orders=Order.objects.filter(driver=driver)
        order_serializer=DriverOrderSerializer(orders,many=True)
        return Response(order_serializer.data)



