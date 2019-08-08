from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Province)
admin.site.register(models.Area)
admin.site.register(models.Place)
admin.site.register(models.AdminPost)
admin.site.register(models.UserPost)
admin.site.register(models.AdminPostComment)
admin.site.register(models.UserPostComment)
admin.site.register(models.AdminPostImage)
admin.site.register(models.UserPostImage)
#admin.site.register(models.Avatar)
#admin.site.register(models.AdminPostEvaluate)
#admin.site.register(models.UserPostEvaluate)