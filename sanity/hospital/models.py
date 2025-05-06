from django.db import models

# Create your models here.
class Articolo(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()

class Hospital():
    def __init__(self, name, region, city, nation):
        self.__nome = name
        self.__regione = region
        self.__città = city
        self.__nazione = nation

class Department(Hospital):
    def __init__(self, name, presidente, member_number):
        self.__name = name
        self.__presidente = presidente
        self.__member_number= member_number


class Citizen():
    def __init__(self, nome, cognome)