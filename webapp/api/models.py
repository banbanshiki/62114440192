from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TentData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class ZipoData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"

class JacketData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class MapData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"    

class CookData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class LEDData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class SleepData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class EqipanoData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"   

class BackData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class BootData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"

class KnifeData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
            

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    date = models.TextField()
    details = models.TextField()

    def __str__(self):
        return f" {self.location}, {self.date}, {self.details}"

    
    
class Forest(models.Model):
    name = models.TextField( verbose_name='ชื่อ')
    image = models.TextField(verbose_name='รูป')
    Level = models.TextField(verbose_name='ความยาก')
    Season = models.TextField(verbose_name='เดือน/ฤดูกาล')
    Stop = models.TextField(verbose_name='ปิดฟื้นฟูธรรมชาติ')
    Distance = models.TextField(verbose_name='ระยะทาง')
    Time = models.TextField(verbose_name='เวลา')
    Details = models.TextField(verbose_name='รายละเอียด')
    
    def __str__(self):
        return f'สถานที่ {self.name} ,{self.image},{self.Level},{self.Season},{self.Stop},{self.Distance},{self.Time},{self.Details}'   
    
class BookfoData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"

class SLData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
            
class ToiletData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"

class CookingData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
    
class PortalData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"     
    
class FirstaidData(models.Model):
    type = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"

   