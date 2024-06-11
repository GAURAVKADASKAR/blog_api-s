from django.db import models



class blog(models.Model):
    title=models.TextField()
    content=models.TextField()


    def __str__(self):
        return self.title
        