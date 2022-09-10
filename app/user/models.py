import logging

from django.contrib.auth.models import AbstractUser

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):

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
