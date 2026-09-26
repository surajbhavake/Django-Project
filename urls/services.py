from .models import URL
from .utils import generate_short_code


def create_url(original_url):
    return URL.objects.create(
        original_url = original_url,
        short_code = generate_short_code(),
    )