from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'role']

    def validate_role(self, value):
        if value not in ['admin', 'manager', 'employee']:
            raise serializers.ValidationError("Invalid role. Choose from 'admin', 'manager', 'employee'.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.get('role', 'employee')  # Default to 'employee' if not provided
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=password,
            role=role,
        
        )
        return user

# class LoginSerializer(serializers.Serializer):
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [ 'username', 'password']

    def validate(self, data):
        # Get the username and password from the request data
        username = data.get('username', None)
        password = data.get('password', None)

        print(f"Username: {username}, Password: {password}")  # Add this line for debugging

        if username is None or password is None:
            raise serializers.ValidationError('Both Username and Password are required')

        # Get the user by username
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Not exist')

        # Check the password
        if not user.check_password( password ):
            raise serializers.ValidationError('Invalid credentials')

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')

        return {'user': user}

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        return data


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'gender', 'age']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance