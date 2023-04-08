from rest_framework import serializers
from page.models import Profile, Page, Posts
from rest_framework.renderers import JSONRenderer


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to deal with json data representation of Profile's model objects
    """
    
    class Meta:
        model = Profile
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    """
    Serializer to deal with json data representation of Page's model objects
    """
    pass


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer to deal with json data representation of Posts's model objects
    """
    pass

