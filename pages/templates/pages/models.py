import uuid as uuid_module
from PIL import Image


from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.gdal import GDALRaster
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.postgres import fields
from django.core.exceptions import ValidationError


from django.contrib.gis.db.models.fields import GeometryField

# Create your models here.


class vols(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid_module.uuid4, unique=True, serialize=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    id_vol = models.IntegerField(default=0)
    donnees = models.CharField(max_length=1500)
    #ortho = models.RasterField()
    orthophoto = GeometryField(null=True, blank=True, srid=4326, help_text="Extent of the orthophoto created by OpenDroneMap")
    dsm_extent = GeometryField(null=True, blank=True, srid=4326, help_text="Extent of the DSM created by OpenDroneMap")
    dtm_extent = GeometryField(null=True, blank=True, srid=4326, help_text="Extent of the DTM created by OpenDroneMap")


#class meteo(models.Model):
#    id
