from rest_framework import serializers
from .models import StoreDriver,Merchant
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            user=Merchant.objects.get(user=user)
            user_type="merchant"
        except:
            try:
                user=StoreDriver.objects.get(driver=user)
                user_type="driver" 
            except:
                user_type=None
        token['user_type'] = user_type


        return token

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=StoreDriver
        fields= ['employee_id',"phone_number","store"]


