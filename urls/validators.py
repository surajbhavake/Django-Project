from urllib.parse import urlparse
from rest_framework import serializers


MAX_URL_LENGTH = 2048

def validate_original_url(value):
    if len(value) > MAX_URL_LENGTH:
        raise serializers.ValidationError(
            f'URL cannot be long than {MAX_URL_LENGTH} characters'
        )
    parsed_url = urlparse(value)

    if parsed_url.scheme not in ('https','http'):
        raise serializers.ValidationError('Only HTTP and HTTPS URLs are allowed')

    if not parsed_url.netloc:
        raise serializers.ValidationError('Enter a valid URL')

    return value