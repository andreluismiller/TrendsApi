from rest_framework import serializers
from page.models import Profile, Page, Posts
from rest_framework.renderers import JSONRenderer



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Page.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'page']




class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)





class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to deal with json data representation of Profile's model objects
    """
    
    class Meta:
        model = Profile
        fields = ('username',)





class PagePublicSerializer(serializers.ModelSerializer):
    """
    Serializer to display only page's public data
    """
    user = ProfileSerializer

    class Meta:
        model = Page
        fields = ['date', 'user', 'pageId', 'followers']



class PostPublicSerializer(serializers.ModelSerializer):
    """
    Serializer to display only posts public data
    """
    user = ProfileSerializer

    class Meta:
        model = Posts
        fields = ['user', 'mediaId', 'type', 'likes', 'plays']





class PageSerializer(serializers.DynamicFieldsModelSerializer):
    """
    Serializer to dinamiclly display private page's fields based on the user request paramns
    """
    user = ProfileSerializer()

    class Meta:
        model = Page
        fields = '__all__'



class PostSerializer(serializers.DynamicFieldsModelSerializer):
    """
    Serializer to dinamiclly display private post's fields based on the user request params
    """
    user = ProfileSerializer()

    class Meta:
        model = Posts
        fields = '__all__'

