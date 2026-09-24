from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = "__all__"
        read_only_fields = [ 'id','short_code','created_at']