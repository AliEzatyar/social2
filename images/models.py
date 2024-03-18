from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_of_user')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="users_pics")
    url = models.URLField(max_length=2000)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200) # in its form, we used slugify to create automatic slug
    description = models.TextField(blank=True)
    users_liked = models.ManyToManyField(AUTH_USER_MODEL, related_name='liked_images')
    # for ordering, couning the amount of users who have liked is an expensive process
    total_likes = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])
        ]
        ordering = ['-total_likes']

    def __str__(self):
        return f"Image caught by {self.user.first_name}."

    # overriding save() * note that we have to finally call super().save()
    def save(self, *args, **kwargs):
        if self.slug in (None,"",''):
            self.slug = slugify(self.title)  # text slugifier
        super().save(*args, **kwargs) # we call it to save as orginally is needed
        print(self.slug,"slug")
        print(self.url)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
