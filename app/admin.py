import imp
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(GalleryImage)
admin.site.register(Video)
admin.site.register(Testimonial)