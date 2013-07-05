from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

class PhoneNo(models.Model):
    contact = models.ForeignKey(Contact)
    phone_no = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.phone_no
