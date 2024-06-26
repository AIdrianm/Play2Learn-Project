import random
import string

from django.utils.text import slugify

def unique_slug(s, model, num_chars=50):
    """
    return the slyug of num_chars length unique to model

    's' is the string to slugify
    'model' is the model to check for uniqueness

    """

    slug = slugify(s)
    slug = slug[:num_chars].strip('-')
    while True:
        dup = model.objects.filter(slug=slug)
        if not dup:
            return slug

        slug = slug[:39] + '-' + random_string(10)
        

def random_string(num_chars=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(num_chars))