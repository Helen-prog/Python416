from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    is_verify_email = models.BooleanField(default=False, verbose_name="Подтверждение электронной почты")


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification object for {self.user.email}"

    def send_verification_email(self):
        link = reverse('email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Подтверждение учетной записи для {self.user.username}"
        message = f"Для подтверждения учетной записи {self.user.email} перейдите по ссылке: {verification_link}"
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [self.user.email]
            )
        except BadHeaderError:
            return HttpResponse("Обнаружен неверный заголовок")

    def is_expired(self):
        return True if now() >= self.expiration else False

    class Meta:
        verbose_name = "верификацию"
        verbose_name_plural = "верификация по почте"
