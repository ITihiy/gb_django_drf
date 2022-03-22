from django.db import models

from drf_users.models import DRFUser


class Project(models.Model):
    name = models.CharField(max_length=256)
    repo = models.URLField()
    users = models.ManyToManyField(DRFUser)


class TODOItem(models.Model):
    todo_text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(DRFUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
