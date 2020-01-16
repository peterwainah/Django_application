from django.contrib import admin
from apply.models import UserProfileInfo, User, ScholarshipApplication ,SchoolInformation ,JustInformation
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(ScholarshipApplication)
admin.site.register(SchoolInformation)
admin.site.register(JustInformation)