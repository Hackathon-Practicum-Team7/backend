import pandas as pd
import pytest

from apps.students.models import Student
from apps.students.utils import get_dataframe


@pytest.mark.django_db
def test_get_dataframe(student, contact):
    students = Student.objects.filter(pk=student.pk)
    student = students.first()
    student.contact = contact
    student.save()
    result = get_dataframe(students)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
