from django.db import models


class User(models.Model):
    name = models.CharField(max_length=191, null=True)
    phone = models.CharField(max_length=191)
    uuid = models.CharField(max_length=36, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    ball = models.IntegerField(default=0)
    birthday = models.DateField(null=True)
    gender = models.BooleanField(default=True)  # Assuming True represents male and False represents female
    lat = models.DecimalField(max_digits=32, decimal_places=16, null=True)
    lng = models.DecimalField(max_digits=32, decimal_places=16, null=True)
    deleted_at = models.DateTimeField(null=True)
    fcm_token = models.CharField(max_length=191, null=True)
    last_updated_personal_at = models.DateTimeField(null=True)
    points_per_visit = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=45, null=True)
    device_type = models.CharField(max_length=191, null=True)

    class Meta:
        db_table = 'users'
