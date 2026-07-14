from django.db import models

class Banner(models.Model):
    rasm = models.ImageField(upload_to="banner/")
    yozuv = models.CharField(max_length=255)

    def __str__(self):
        return self.yozuv

from django.db import models


class JanrCategory(models.Model):
    id = models.AutoField(primary_key=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class DavlatCategory(models.Model):
    id = models.AutoField(primary_key=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class YilCategory(models.Model):
    id = models.AutoField(primary_key=True)
    yil = models.IntegerField()

    def __str__(self):
        return str(self.yil)


class Kino(models.Model):
    id = models.AutoField(primary_key=True)

    nomi = models.CharField(max_length=255)

    janr = models.ForeignKey(
        JanrCategory,
        on_delete=models.CASCADE
    )

    davlat = models.ForeignKey(
        DavlatCategory,
        on_delete=models.CASCADE
    )

    yil = models.ForeignKey(
        YilCategory,
        on_delete=models.CASCADE
    )

    tili = models.CharField(max_length=255)
    davomiyligi = models.CharField(max_length=100)
    yosh = models.CharField(max_length=100)
    izoh = models.TextField()

    def __str__(self):
        return self.nomi