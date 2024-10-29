from rest_framework.decorators import api_view
from rest_framework.response import Response

from bf_task.auth_app.serializers import RegistrationSerializer


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email

        else:
            data = serializer.errors

        return Response(data, status=201)