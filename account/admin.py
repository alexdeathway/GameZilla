from django.contrib import admin
from .models import ProfileModel
#from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# from .forms import CustomUserCreationForm

admin.site.register(ProfileModel)

# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = CustomUserCreationForm

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'user is guest', {
#                 'fields': (
#                     'guest',
#                 )
#             }
#         )
#     )


# admin.site.register(User, CustomUserAdmin)
