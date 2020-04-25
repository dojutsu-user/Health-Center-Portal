import pytest

from ddf import G

from django.contrib.auth.models import User

from doctor.models import Doctor
from medicines.models import Medicine
from student.models import Student


@pytest.fixture
def student(db):
    user = G(User)
    student = G(Student, user=user.pk)
    return student


@pytest.fixture
def doctor(db):
    user = G(User)
    doctor = G(Doctor, user=user.pk)
    return doctor

@pytest.fixture
def create_medicines(db):
    for _ in range(10):
        G(Medicine)
