from ckeditor.fields import RichTextField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profil(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField('profil/')
    description = models.TextField()

    def __str__(self):
        return self.name


class SocialLink(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f'{self.name} {self.url}'


class Post(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField('post/')
    description = models.TextField()
    body = RichTextField()

    def __str__(self):
        return self.title


class About(BaseModel):
    body = RichTextField()


