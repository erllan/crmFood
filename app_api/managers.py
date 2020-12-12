from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, login, email, name, surname, password, phone=None, ):
        if login is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(name=name, email=self.normalize_email(email), login=login, phone=phone, surname=surname)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, email, name, surname, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(login, email, name, surname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
