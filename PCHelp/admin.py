from django.contrib import admin
from .models import Client, FeedbackType, Bid, Сomment, Work, Staff, Roles

class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','numberphone','email')
    list_display_links = ('firstname','lastname','numberphone')
    search_fields = ('firstname','lastname','numberphone','email')

class BidAdmin(admin.ModelAdmin):
    list_display = ('id','client','textbid','datecreation')
    search_fields = ('id','textbid')

class СommentAdmin(admin.ModelAdmin):
    list_display = ('client','textcomment','datecreation')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('nameWork','description','price')

class FeedbackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'option')

class StaffTypeAdmin(admin.ModelAdmin):
    list_display = ('id','role','firstname','lastname')

class RolesTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(Work, WorkAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(FeedbackType,FeedbackTypeAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Сomment,СommentAdmin)
admin.site.register(Staff,StaffTypeAdmin)
admin.site.register(Roles,RolesTypeAdmin)