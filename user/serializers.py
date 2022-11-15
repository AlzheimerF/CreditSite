from rest_framework import serializers
from .models import Profile, Info, SecretInfo

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'status', 'password', 'password2', 'date_joined', ]

    def validate(self, attrs):
        if attrs['password2'] != attrs['password']:
            raise serializers.ValidationError()
        return attrs

    def create(self, validated_data):
        profile = Profile.objects.create(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            status=validated_data.get('status'),
            about_yourself=validated_data.get('about_yourself')
        )

        return profile


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ['user', 'country', 'city', 'language', 'age', 'gender', ]

    def create(self, validated_data):
        info = Info.objects.create(
            user=validated_data.get('user'),
            country=validated_data.get('country'),
            city=validated_data.get('city'),
            language=validated_data.get('language'),
            age=validated_data.get('age'),
            gender=validated_data.get('gender')
        )
        return info