# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny

# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(email=email, password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh),
#             }, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
