from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user
        objects = Advertisement.objects.filter(status='OPEN', creator=user)
        method = self.context['request'].method
        status = self.initial_data.get('status')

        if len(objects) >= 10 and method == 'POST':
            raise ValidationError('Превышено кол-во открытых объявлений')
        if len(objects) >= 10 and method == 'PATCH' and status == 'OPEN':
            raise ValidationError('Превышено кол-во открытых объявлений')

        return data
