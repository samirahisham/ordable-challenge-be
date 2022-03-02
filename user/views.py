from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# class userLogin(APIView):
#     def post(self, request, *args,  **kwargs):
#         email = request.data['email']
#         password = request.data['password']
#         if email is None:
#             return Response("ERRR")
#         elif password is None:
#             return Response("errrr")

#         # authentication user
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return Response("success")
#         return Response("erRRRRRR")

