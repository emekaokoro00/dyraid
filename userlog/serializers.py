from models import UserLog
from rest_framework import viewsets, serializers
from home.serializers import UserSerializer

class UserLogSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    log_time = serializers.DateTimeField()
    comment = serializers.CharField(required=False, max_length=100)
    class Meta:
        model = UserLog
        fields = ('user', 'log_time', 'comment')   
        
    def create(self, validated_data):
        """
        Create and return a new UserLog
        """ 
        return UserLog.objects.create(**validated_data)