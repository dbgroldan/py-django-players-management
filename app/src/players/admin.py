from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from src.players.models import *


class TelephoneInline(admin.StackedInline):
    model = Telephone
    fk_name = 'user_id'

class CubesInline(admin.StackedInline):
    model = Cube.users.through

class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        CubesInline,
    ]

class CubePlayerAdmin(admin.ModelAdmin):
    inlines = [
        TelephoneInline,
        CubesInline,
    ]
    exclude = ('users', )


admin.site.register(Player, CubePlayerAdmin)
admin.site.register(PlayerReview)

