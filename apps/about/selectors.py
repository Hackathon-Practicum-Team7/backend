from apps.about.models import City, DirectionOfStudy


def get_cities():
    return City.objects.all().order_by("title")


def get_direction_of_study():
    return DirectionOfStudy.objects.all().prefetch_related("professions")
