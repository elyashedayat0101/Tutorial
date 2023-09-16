from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is Required")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.using(self._db)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
