from django.db import models


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

''' References:
https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-fiels-type
https://docs.djangoproject.com/en/1.10/ref/models/fields/

'''