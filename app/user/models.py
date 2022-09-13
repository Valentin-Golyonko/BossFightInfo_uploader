import logging

from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core.utility_scripts.core_constants import CoreConstants

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):
    auth_str = models.CharField(
        max_length=256,
        default="",
    )
    dude_id = models.PositiveIntegerField(default=0)
    is_email_confirmed = models.BooleanField(default=False)
    gw2_account_name = models.CharField(
        max_length=CoreConstants.GW2_ACCOUNT_LEN,
        default='',
        blank=True,
        verbose_name="GW2 Account",
    )

    def save(self, *args, **kwargs):
        if self.dude_id == 0:
            return None
        elif CustomUser.objects.filter(dude_id__gt=0).count() > 0:
            return None

        if not self.is_superuser:
            self.is_staff = False
            self.is_superuser = False
            self.is_active = True
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"CustomUser [{self.id}]"

    class Meta:
        ordering = ('-id',)
