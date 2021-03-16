import django_filters
from .models import Subject,Teacher

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = 'lastName'

class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = 'name'