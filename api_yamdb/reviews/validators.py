from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    now = timezone.now()
    if value > now.year:
        raise ValidationError(
            'Значение больше текущего года!'
        )
    if value < 1900:
        raise ValidationError(
            'Значения меньше 1900 не допускаются!'
        )
    return value
