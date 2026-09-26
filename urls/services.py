from .models import URL
from .utils import generate_short_code


def create_url(original_url):
    return URL.objects.create(
        original_url = original_url,
        short_code = generate_short_code(),
    )

def get_url_by_id(pk):
    return URL.objects.filter(pk=pk).first()

def delete_url(url):
    url.delete()