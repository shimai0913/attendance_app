from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = get_user_model()
        model = User
        # fields = ('id', 'username',)
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            # 'full_name',
            'phone_number',
            'email',
            'employee_id',
            )
        # fields = '__all__'
