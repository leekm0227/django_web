from django.contrib import admin
from api.models import *


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'type')


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('output_name', 'input_list')

    @staticmethod
    def output_name(obj):
        return obj.output.name

    @staticmethod
    def input_list(obj):
        return " | ".join([i.name for i in obj.input.all()])


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 10


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
    inlines = (InventoryInline,)

    @staticmethod
    def user_name(obj):
        return obj.user.username