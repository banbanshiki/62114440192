from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forests(models.Model):
    name = models.TextField( verbose_name='ชื่อ')
    image = models.ImageField(upload_to='images' , verbose_name='รูป')
    Level = models.TextField(verbose_name='ความยาก')
    Season = models.TextField(verbose_name='เดือน/ฤดูกาล')
    Distance = models.TextField(verbose_name='ระยะทาง')
    Time = models.TextField(verbose_name='เวลา')
    Details = models.TextField(verbose_name='รายละเอียด')
    
    def __str__(self):
        return f'สถานที่ {self.name} ,{self.image},{self.Level},{self.Season},{self.Distance},{self.Time},{self.Details}'

class Medics(models.Model):
    Symptom = models.TextField( verbose_name='อาการ')
    Remedy = models.TextField( verbose_name='วิธีรักษา')

    def __str__(self):
            return f'ปฐมพยาบาล {self.Symptom},{self.Remedy}'

class Cookings(models.Model):
    Menu = models.TextField( verbose_name='เมนู')
    Rawmaterial = models.TextField( verbose_name='วัตถุดิบ')
    Method = models.TextField( verbose_name='วิธีทำ')

    def __str__(self):
            return f'วิธีประกอบอาหาร {self.Menu},{self.Rawmaterial},{self.Method}'

class Crafts(models.Model):
    Menu = models.TextField( verbose_name='เมนู')
    Method = models.TextField( verbose_name='วิธีทำ')

    def __str__(self):
            return f'การคราฟ {self.Menu},{self.Method}'           

# class Diary(models.Model):
#     NumberOfSteps = models.TextField( verbose_name='จำนวนก้าว')
#     Distance = models.TextField(verbose_name='ระยะทาง')
#     Days = models.TextField(verbose_name='วันที่')
#     Name = models.TextField(verbose_name='สถานที่เดินป่า')
#     Details = models.TextField(verbose_name='รายละเอียด')
    
#     def __str__(self):
#         return f'ไดอารี่ {self.NumberOfSteps},{self.Distance},{self.Days},{self.Name},{self.Details}'            