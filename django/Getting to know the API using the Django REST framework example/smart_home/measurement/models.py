from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photo')

    def __str__(self):
        return f'{self.sensor_id.name}: Показания на {self.date}'