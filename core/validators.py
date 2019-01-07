import re
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_human_name(value):

    regex = r'^[A-Za-z\s\-]+$'
    if not re.match(regex, value):
        raise ValidationError(
            'Names can contain only alpha characters',
            code='invalid')
