from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers import UserSerializer, RegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):  # user viewset
    serializer_class = UserSerializer  # calls user serializer
    queryset = User.objects.all()  # retrieves all users
    permission_classes = (TokenAuthentication,)  # must have token to view user


@api_view(['POST', ])
def registration_view(request):  # creating new user
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user."
            data['username'] = user.username
            data['email'] = user.email

        else:
            data = serializer.errors
        return Response(data)
