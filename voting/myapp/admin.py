from django.contrib import admin
from .models import *



admin.site.site_header="Admin Interface"
admin.site.site_title="Admin"
admin.site.index_title="welcome"
# Register your models here.

admin.site.register(voter)
admin.site.register(parties)

class dvote_box(admin.ModelAdmin):
    def has_read_permission(self, request):
        return False
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
   


admin.site.register(vote_box,dvote_box)

