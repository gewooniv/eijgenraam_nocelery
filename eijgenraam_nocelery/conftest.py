#!/usr/bin/env python3
import pytest

from eijgenraam_nocelery.users.models import User
from eijgenraam_nocelery.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()
