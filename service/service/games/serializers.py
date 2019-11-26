from rest_framework import serializers
from games.models import VideoGame


class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGame
        fields = ['id', 'title_name', 'genre', 'rating', 'platform', 'release_date']
