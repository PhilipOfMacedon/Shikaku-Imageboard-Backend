from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Gallery)
admin.site.register(Media)
admin.site.register(PickedCollection)
admin.site.register(MediaFormat)
admin.site.register(FileType)
admin.site.register(Tag)
admin.site.register(UserMediaInteraction)
admin.site.register(UserGalleryInteraction)
admin.site.register(UserPCInteraction)
admin.site.register(MediaCollectionInteractionInfo)