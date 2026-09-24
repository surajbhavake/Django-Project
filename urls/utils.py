import random
import string
from .models import URL
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:

        code =  "".join(
            random.choices(characters,k=length)
        )

        if not URL.objects.filter(short_code = code).exists():
            return code