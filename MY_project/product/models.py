from django.db import models
from helper.models import TimeStamp, generate_unique_slug


class Category(TimeStamp):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childs', on_delete=models.DO_NOTHING)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]
        ordering = ['id']

    def __str__(self):
        name = self.name
        if self.parent:
            name = name + ' – ' + self.parent.name
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.name) > 0:
                self.slug = generate_unique_slug(self)

        super(Category, self).save(*args, **kwargs)


class Active_substance(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Release_form(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Pharm_group(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Drug(TimeStamp):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    active_substance = models.ForeignKey(Active_substance, null=True, blank=True, related_name='drug_substance', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    release_form = models.ForeignKey(Release_form, null=True, blank=True, related_name='drug_form', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, related_name='drug_brand', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='drug_category', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, blank=True, related_name='drug_country', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, related_name='drug_manufacturer', on_delete=models.CASCADE)
    pharm_group = models.ForeignKey(Pharm_group, null=True, blank=True, related_name='drug_group', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)

    def __str__(self):
        return (self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.name) > 0:
                self.slug = generate_unique_slug(self)

        super(Drug, self).save(*args, **kwargs)

class Photo(models.Model):
    image = models.ImageField(upload_to='drug_images', null=True, blank=True)
    drug = models.ForeignKey(Drug, null=True, blank=True, related_name='drug_image', on_delete=models.CASCADE)

