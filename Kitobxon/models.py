from django.db import models

class Muallif(models.Model):
    ismi = models.CharField(max_length=20)
    familiyasi = models.CharField(max_length=20)
    tugilgan_sanasi = models.DateField()
    asarlar_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.ismi} {self.familiyasi}'

class Kitob(models.Model):
    Janrlar = (
        ('Roman', 'roman'),
        ('Qissa', 'qissa'),
        ('Hikoya', 'hikoya')
    )
    nomi = models.CharField(max_length=40)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yozilgan_sana = models.DateField()
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=10, choices = Janrlar)

    def __str__(self):
        return f'{self.nomi}'

class Record(models.Model):
    FIO = models.CharField(max_length=40)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()

    def __str__(self):
        return f'{self.FIO}'