from django.contrib import admin

# Register your models here.


from .models import Post, Comments


class postAdmin(admin.ModelAdmin):
    list_display = ['id_post','title','date_post','author']


class commentAdmin(admin.ModelAdmin):
        list_display = ['id_comment','content','post','date_post','commentator']


admin.site.register(Post, postAdmin)
admin.site.register(Comments, commentAdmin)