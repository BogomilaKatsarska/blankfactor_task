from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'Error': 'Passwords do not match'}
            )

        if UserModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'Error': 'Email already registered'}
            )

        account = UserModel(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        account.set_password(password)
        account.save()

        return account