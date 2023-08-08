from django import forms
from django.core.validators import RegexValidator
from .models import User


class UserForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=9,
        min_length=9,
        validators=[RegexValidator(r'^[0-9]+$', 'Please enter a numeric phone number.')]
    )

    class Meta:
        model = User
        exclude = (
            'uuid',
            'ball',
            'phone',
            'birthday',
            'gender',
            'lat',
            'lng',
            'deleted_at',
            'fcm_token',
            'last_updated_personal_at',
            'points_per_visit',
            'created_at',
            'updated_at',
            'ip_address',
            'device_type'
        )

