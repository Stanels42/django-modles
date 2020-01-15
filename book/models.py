from django.db import models

# Create your models here.
class Data(models.Model):
  title = models.CharField(max_length=128)
  author = models.CharField(max_length=128)
  about = models.TextField()
  user = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.title
