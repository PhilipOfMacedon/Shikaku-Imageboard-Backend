from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=24)
    email = models.EmailField(max_length=254)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        join = self.date_joined.strftime('%a %d %b %Y, %I:%M%p')
        seen = self.last_seen.strftime('%a %d %b %Y, %I:%M%p')
        return f"{self.username} ({self.email}) Joined: {join}; Last seen: {seen}"

class Gallery(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True) 
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, on_delete=models.PROTECT)

class PickedCollection(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

class MediaFormat(models.Model):
    description = models.CharField(max_length=64)

class FileType(models.Model):
    extension = models.CharField(max_length=8)
    format = models.ForeignKey(MediaFormat, on_delete=models.PROTECT)

class Media(models.Model):
    name = models.CharField(max_length=128, null=True)
    description = models.TextField(blank=True)
    static_path = models.CharField(max_length=512)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_parent_gal_thumb = models.BooleanField(default=False)
    custom_order = models.IntegerField(unique=True)
    parent_gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT)
    media_format = models.ForeignKey(MediaFormat, on_delete=models.PROTECT)

class Tag(models.Model):
    name = models.CharField(max_length=32)
    gallery_set = models.ManyToManyField(Gallery)
    media_set = models.ManyToManyField(Media)

class UserMediaInteraction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    media_id = models.ForeignKey(Media, on_delete=models.PROTECT)
    rate = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    favorite = models.BooleanField(default=False)

class UserGalleryInteraction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    gallery_id = models.ForeignKey(Gallery, on_delete=models.PROTECT)
    rate = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    favorite = models.BooleanField(default=False)

class UserPCInteraction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    pc_id = models.ForeignKey(PickedCollection, on_delete=models.PROTECT)
    rate = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    favorite = models.BooleanField(default=False)

class MediaCollectionInteractionInfo(models.Model):
    media_id = models.ForeignKey(Media, on_delete=models.PROTECT)
    pc_id = models.ForeignKey(PickedCollection, on_delete=models.PROTECT)
    rate = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    favorite = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    custom_order = models.IntegerField(unique=True)