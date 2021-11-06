from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='user', null=True)
    name = models.CharField(max_length = 30, default='No name')
    desc = models.TextField(max_length = 250, default='No info About me')
    github_link = models.CharField(max_length = 100, null=True)
    linkedIn_link = models.CharField(max_length = 100, null=True)
    images = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='project', null=True)
    name = models.CharField(max_length = 30)
    desc = models.TextField(max_length = 250)
    link = models.CharField(max_length = 100, null=True)
    images = models.TextField(max_length = 200, null=True)

    def __str__(self):
        return self.name