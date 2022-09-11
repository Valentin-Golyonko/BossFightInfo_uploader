import logging

from django.contrib.auth.models import AbstractUser
from django.db import models

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):
    auth_str = models.CharField(
        max_length=256,
        default="",
    )

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.is_staff = False
            self.is_superuser = False
            self.is_active = True
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"CustomUser [{self.id}]"

    class Meta:
        ordering = ('-id',)
