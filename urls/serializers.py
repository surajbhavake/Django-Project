from rest_framework import serializers
from .models import URL
from .validators import validate_original_url

class URLSerializer(serializers.ModelSerializer):

    original_url = serializers.CharField(
        validators =[validate_original_url]
    ) #model alway create serializer field automatically we are just overriding so we
    #can customlly validate it 
    class Meta:
        model = URL
        fields = "__all__"
        read_only_fields = [ 'id','short_code','created_at']