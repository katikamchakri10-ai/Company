from django.contrib import admin
from.models import price
# Register your models here.
from .models import about1
from.models import ourteam
from.models import client
from.models import article
from .models import contactforms
admin.site.register(about1)
admin.site.register(ourteam)
admin.site.register(client)
admin.site.register(article)
admin.site.register(price)
admin.site.register(contactforms)