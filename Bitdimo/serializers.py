from rest_framework import serializers
from . import  models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class AdminPostSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many = True)
    placename = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    areaname = serializers.ReadOnlyField()
    longtitude_of_place = serializers.ReadOnlyField()
    latitude_of_place = serializers.ReadOnlyField()
    class Meta:
        model = models.AdminPost
        fields = ('placename', 'areaname', 'created_at', 'number_of_like',
                    'number_of_comment', 'content', 'address', 
                    'longtitude_of_place', 'latitude_of_place', 'images')

class AdminPostCommentSerializer(serializers.ModelSerializer):
    nameuser = serializers.ReadOnlyField()
    urlavatar = serializers.ReadOnlyField()
    class Meta:
        model = models.AdminPostComment
        fields = ('nameuser', 'urlavatar', 'content')

class DetailAdminPostSerializer(serializers.ModelSerializer):
    comments = AdminPostCommentSerializer(many = True)
    #placename = serializers.ReadOnlyField()
    
    class Meta:
        model = models.AdminPost
        fields = ('comments',)

class UserPostSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many = True)
    username = serializers.ReadOnlyField()
    urlavatar = serializers.ReadOnlyField()
    #areaname = serializers.ReadOnlyField()
    class Meta:
        model =  models.UserPost    
        fields = ('username', 'urlavatar', 'created_at', 'number_of_like',
                     'number_of_comment', 'content', 'address', 
                     'longtitude', 'latitude', 'images')

""" 
class UserPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPostImage
        fields = '__all__'
 """