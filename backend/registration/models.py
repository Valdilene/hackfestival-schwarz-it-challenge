import random
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


def code_generator(length=5):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


class RegistrationProfile(models.Model):
    code = models.CharField(
        verbose_name='code',
        max_length=10,
        default=code_generator,
        help_text='random code used for registration and for password reset',
    )
    user = models.OneToOneField(
        verbose_name='user',
        to=User,
        related_name='registration_profile',
        on_delete=models.CASCADE
    )
    code_type = models.CharField(
        verbose_name='code type',
        max_length=2,
        choices=(
            ('RV', 'Registration Validation'),
            ('PR', 'Password Reset')
        )
    )

    def __str__(self):
        return f'{self.user.email}, {self.code}'


@receiver(post_save, sender=User)
# Whenever a user is being created or saved, we want to check if that user has a Registration Profile,
# if not, we want to create one.
def create_registration_profile(sender, instance, **kwargs):
    # get_or_create retrieves an object from the database if it exists,
    # or creates a new object with default values if it does not.
    profile, created = RegistrationProfile.objects.get_or_create(user=instance)
    if created:
        profile.save()
