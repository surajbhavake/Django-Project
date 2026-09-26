from .models import URL
from .utils import generate_short_code
from django.db import IntegrityError
from .exceptions import URLCreationError


def create_url(original_url):
    try:
        return URL.objects.create(
            original_url = original_url,
            short_code = generate_short_code(),
        )
    except IntegrityError as exc: #exc is simply a variable it can be anything e,ab 
        raise URLCreationError(
            'Unable to create the short URL'
        ) from exc

def get_url_by_id(pk):
    return URL.objects.filter(pk=pk).first()

def delete_url(url):
    url.delete()