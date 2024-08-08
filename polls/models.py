from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Polls(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class PollOptions(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    option = models.CharField(max_length=255, unique=True)
    vote = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)