from rest_framework import permissions
from merchants.models import StoreMerchant

class CanManageStore(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            if request.user.merchant.is_admin :
                return True
            return False       
        except:
            return False

