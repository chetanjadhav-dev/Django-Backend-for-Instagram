from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from contents.serializers import UserSerializer,UserLoginSerializer
from contents.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CreatUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserView(APIView):

    def post(self, request):
        # request.data (email, password)
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                if user.password == serializer.validated_data['password']:
                    token = Token.objects.get_or_create(user=user)

                    return Response({'success': True, 'token': token[0].key})
                else:
                    return Response({'success': True, 'message': 'incorrect password!!!'})
                
            except ObjectDoesNotExist:
                return Response({'success': False, 'message': 'user does not exist!!!'})


class RetriveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': f'{list(request.data.keys())[0]} is updated'})
        else:
            print(serializer.errors)
            return Response({'success': False, 'message': 'error updating the user'})


class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk):
        if pk == request.user.id:
            self.perform_destroy(request.user)

            return Response({'success': True, 'message': 'user deleted successfully!'})
        else:
            return Response({'success': False, 'message': 'invalid authentication!'})
