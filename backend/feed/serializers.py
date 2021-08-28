from rest_framework import serializers
from feed.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
