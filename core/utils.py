from django.utils import timezone


def current_academic_year():
    """
    Returns the current academic year.
    Example:
    2026/2027
    """

    year = timezone.now().year

    return f"{year}/{year + 1}"