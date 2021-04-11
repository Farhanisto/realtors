from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
User = get_user_model()

class SignupView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request, format= None):
    data = self.request.data
    name = data['name']
    email = data['email']
    password = data['password']
    password2 = data['password2']
    
    if password == password2:
      if User.objects.filter(email=email).exists():
        return Response("This email exist.. Try again")
      else:
        if len(password2) < 6:
          return Response({"error": 'password should be longer than 6 charracters'})
        else:
          user = User.objects.create_user(email=email,name=name,password = password)
          user.save()
          return Response({"Success": "user created"})

    return Response("passwords do not match")
