from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from blog.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_attr = [attr.name for attr in Account._meta.fields]
    list_display=tuple(list_attr)

admin.site.register(Account, AccountAdmin)
app_models = apps.get_app_config('blog').get_models()
# for model in app_models:
#     # try:
#         admin.site.register(model)
#     # except AlreadyRegistered:
#     #     pass
