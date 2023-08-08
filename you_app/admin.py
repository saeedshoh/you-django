from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html

from .models import User

from .forms import UserForm

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        'id',
        'display_avatar',
        'name',
        'phone',
        'ball',
        'created_at',
        'action_buttons'
    )
    list_display_links = ('id', 'name')
    ordering = ()
    search_fields = ('name', 'phone')
    form = UserForm

    def display_avatar(self, obj):
        return format_html('<img src="{}"  width="25"/>'.format(obj.avatar.url))
    display_avatar.short_description = 'Аватарка'

    def action_buttons(self, obj):
        return format_html('<a href="/history/">Показать история баллов</a>'.format(obj.id))

    action_buttons.short_description = 'Действии'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('history', self.admin_site.admin_view(self.custom_view), name='custom_view'),
        ]
        return custom_urls + urls

    def custom_view(self, request):
        # Ваш код для создания содержимого страницы
        # Можете использовать шаблоны или формировать HTML прямо здесь
        context = {
            'message': 'Это ваша кастомная страница!',
        }
        return render(request, 'admin/custom_view.html', context)

