from django.contrib import admin
from django.db.models import Case, When, Value
from django.utils.translation import ugettext as _

from apps.donations.models import Institution, Donation, Category


def get_categories(obj):
    return ", ".join([cat.name for cat in obj.categories.all()])


get_categories.short_description = _('Kategorie')


def donation_archive(modeladmin, request, queryset):
    queryset.update(is_taken=Case(
        When(is_taken=True, then=Value(False)),
        When(is_taken=False, then=Value(True)),
    ))


donation_archive.short_description = _('Zmień status darowizny')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', get_categories]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'institution', 'user', get_categories, 'is_taken']
    exclude = ['user']
    actions = [donation_archive]
