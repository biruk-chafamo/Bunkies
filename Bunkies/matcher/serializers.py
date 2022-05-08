from django.contrib.auth.password_validation import validate_password

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'url', 'username', 'first_name', 'last_name',
            'email', 'password', 'password2',
        ]

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', '')
        validated_data.pop('password2', '')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ListUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name']  # TODO: remove friends from list


class ConnectionRequestSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, attrs):
        sender = self.context.get('request').user
        receiver = attrs.get('receiver')
        connection_type = attrs.get('connection_type')

        if sender == receiver:
            raise serializers.ValidationError({"receiver": f'you cannot send a connection request to yourself.'})
        if sender in receiver.connections.filter(connection__connection_type=connection_type,
                                                 connection__sender=sender, connection__is_accepted=False):
            raise serializers.ValidationError({"receiver": f'connection to {receiver.username} is already requested.'})
        if sender in receiver.connections.filter(connection__connection_type=connection_type,
                                                 connection__sender=sender, connection__is_accepted=True):
            raise serializers.ValidationError({"receiver": f'{receiver.username} is already your connection.'})
        return attrs

    class Meta:
        model = Connection
        fields = ['url', 'sender', 'receiver', 'connection_type']
        read_only_fields = ['sender']


class AcceptConnectionRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['url', 'sender', 'receiver', 'is_pending', 'is_accepted']
        read_only_fields = ['sender', 'receiver']
