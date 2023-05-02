from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User


# Create your models here.

## API Data model

class System(models.Model):
    name = models.CharField(max_length=250, default="<name>")
    satelliteid = models.CharField(max_length=16, default="")
    vendor = models.CharField(max_length=250, default="<vendor>")
    systemservices = models.CharField(max_length=250, default="<systemservices>")
    service = models.CharField(max_length=500, default="<service>")
    API = models.CharField(max_length=100, default="<api address>")
    company_logo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    contract = models.CharField(max_length=100, default="<contract>")
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '|' + self.satelliteid


class Battery(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    charge = models.CharField(max_length=16, default="")
    level = models.CharField(max_length=16, default="")
    counter = models.IntegerField(default="0")

    @property
    def battery(self):
        if self.level >= 85:
            return self.charge("Green")
        elif 55 <= self.level > 85:
            self.counter +=1
            return self.charge("Yellow")
        else:
            self.counter += 1
            return self.charge("Red")

#        match level:
#            case int() if 85 <= level:
#                return ...
#            case int() if 55 <= level < 85:
#                return ...
#            case int() if level < 55:
#                return ...
#            case _:
#                raise ValueError("invalid level value")  # panic!

    def __str__(self):
        return self.system + '|' + self.level

class TSTAT(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    tstatlevel = models.CharField(max_length=16, default="")
    level = models.CharField(max_length=16, default="")
    counter = models.IntegerField(default="0")

    @property
    def tstatcondition(self):
        if self.level >= 85:
            return self.tstatlevel("Green")
        elif 55 <= self.level > 85:
            self.counter +=1
            return self.tstatlevel("Yellow")
        else:
            self.counter += 1
            return self.tstatlevel("Red")

#        match level:
#            case int() if 85 <= level:
#                return ...
#            case int() if 55 <= level < 85:
#                return ...
#            case int() if level < 55:
#                return ...
#            case _:
#                raise ValueError("invalid level value")  # panic!

    def __str__(self):
        return self.system + '|' + self.level

class Event(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=25, default="")
    satelliteid = models.CharField(max_length=16, default="")
    redhighlimit = models.CharField(max_length=16, default="")
    yellowhighlimit = models.CharField(max_length=16, default="")
    redlimitlow = models.CharField(max_length=16, default="")
    yellowlimitlow = models.CharField(max_length=16, default="")
    rawvalue = models.CharField(max_length=16, default="")
    component = models.CharField(max_length=16, default="")

    def __str__(self):
        return self.rawvalue + '|' + self.component + '|' + self.timestamp + '|'