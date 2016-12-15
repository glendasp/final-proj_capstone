from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp


# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    # Customizing how adm works: displaying what I want to see
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     list_display = ["__unicode__", "date_created", "updated"]
    #     model = SignUp


admin.site.register(SignUp, SignUpAdmin)

''' Reference:
https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
'''
