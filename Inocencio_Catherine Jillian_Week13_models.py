
from django.db import models


class GuestbookEntry(models.Model):
    name = models.CharField(max_length=80)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
