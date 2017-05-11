from django.contrib.auth.models import User
from rest_framework import viewsets, serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')    
    
# class UserLogList(viewsets.ModelViewSet):
#     model = UserLog
#     context_object_name = 'userlog_list' 
#     def get(self):
#         userlog_list = super(UserLogList, self).get_queryset()
#         search_comment = self.request.GET.get('search_comment')
#         if search_comment:
#             userlog_list = userlog_list.filter(comment__icontains=search_comment)
#         return userlog_list