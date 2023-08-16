from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username: str, first_name: str, password: str, telegram_id: str = None) -> 'User':
        if not username:
            raise ValueError("`username` was not be given")
        user = self.model(
            username=username,
            first_name=first_name,
            telegram_id=telegram_id
        )

        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=150,
        null=True,
        blank=True,
    )
    telegram_id = models.CharField(
        verbose_name='telegram id',
        max_length=32,
        null=True,
        blank=True
    )
    USERNAME_FIELD = "username"
    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username
