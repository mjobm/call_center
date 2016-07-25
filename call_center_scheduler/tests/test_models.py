import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestRequest:
    def test_init(self):
        request = mixer.blend("call_center_scheduler.Request")
        assert request.pk == 1, "should have an instance"
