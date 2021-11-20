from django.contrib.admin.sites import site
from django.db import models

# Create your models here.
class MessageContact(models.Model):
    class Meta:
        verbose_name = 'Message' 
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    message = models.TextField()
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0} {1} {2} {3} {4} {4}'.format(
            self, self.name, self.email, self.title, self.message, self.visibility
        )

    def __str__(self):
        return self.title