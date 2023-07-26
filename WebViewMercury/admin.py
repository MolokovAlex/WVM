from django.contrib import admin

# Register your models here.

from .models import DBC, DBG, DBGC, DBPP, DBIC

admin.site.register(DBC)
admin.site.register(DBG)
admin.site.register(DBGC)
admin.site.register(DBPP)
admin.site.register(DBIC)