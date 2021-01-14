from rest_framework import serializers

from api_user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # 모델 User의 모든 field를 serializer한다.