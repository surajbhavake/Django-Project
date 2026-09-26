from urllib.parse import urlparse
from rest_framework import serializers

def validate_original_url(value):
    parsed_url = urlparse(value)

    if parsed_url.scheme not in ('https','http'):
        raise serializers.ValidationError('Only HTTP and HTTPS URLs are allowed')

    if not parsed_url.netloc:
        raise serializers.ValidationError('Enter a valid URL')

    return value