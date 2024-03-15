from django.db import models

class Plants(models.Model):
    plants_id=models.AutoField(primary_key=True)
    plants_name=models.CharField(max_length=60)
    def __str__(self):
        return self.plants_name
class Plants4(models.Model):
    plants_id=models.AutoField(primary_key=True)
    plants_name=models.CharField(max_length=60)
    def __str__(self):
        return self.plants_name

class Plant(models.Model):

    plants_name=models.ForeignKey(Plants,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.plants_name)

class Diseases(models.Model):
    case_id=models.AutoField(primary_key=True)
    plant=models.ForeignKey(Plants4,on_delete=models.CASCADE)
    disease=models.CharField(max_length=100)
    explain=models.CharField(max_length=500,null=True,blank=True)
    treatment=models.CharField(max_length=200)
    protection=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.case_id)
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name

class CountryCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class news(models.Model):
    img=models.ImageField(upload_to='photos')
    time=models.DateField()
    case=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    plant=models.ForeignKey(Plants,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.time)


class Country1(models.Model):

    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.country_name)

class City1(models.Model):

    city_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country1, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city_name', 'country')

    def __str__(self):
        return str(self.city_name)

class CountryCity1(models.Model):
    city = models.ForeignKey(City1, on_delete=models.CASCADE)
    country = models.ForeignKey(Country1, on_delete=models.CASCADE)

class news1(models.Model):
    img=models.ImageField(upload_to='photos')
    time=models.DateField()
    case=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    city=models.ForeignKey(City1,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(Country1,on_delete=models.CASCADE,null=True,blank=True)
    plant=models.ForeignKey(Plants,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.time)

class Plants2(models.Model):
    plants_id=models.AutoField(primary_key=True)
    plants_name=models.CharField(max_length=60)
    def __str__(self):
        return self.plants_name



class Country2(models.Model):
    country_id=models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.country_name)

class City2(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country2, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city_name', 'country')

    def __str__(self):
        return str(self.city_name)

class CountryCity2(models.Model):
    city = models.ForeignKey(City2, on_delete=models.CASCADE)
    country = models.ForeignKey(Country2, on_delete=models.CASCADE)

class news2(models.Model):
    img=models.ImageField(upload_to='photos')
    time=models.DateField()
    case=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    city=models.ForeignKey(City2,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(Country2,on_delete=models.CASCADE,null=True,blank=True)
    plant=models.ForeignKey(Plants,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.time)



class Plants3(models.Model):
    plants_id=models.AutoField(primary_key=True)
    plants_name=models.CharField(max_length=60)
    def __str__(self):
        return str(self.plants_id)



class Country3(models.Model):
    country_id=models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.country_name)

class City3(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country3, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city_name', 'country')

    def __str__(self):
        return str(self.city_name)

class CountryCity3(models.Model):
    city = models.ForeignKey(City3, on_delete=models.CASCADE)
    country = models.ForeignKey(Country3, on_delete=models.CASCADE)

class news3(models.Model):
    img=models.ImageField(upload_to='photos')
    time=models.DateField()
    case=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    city=models.ForeignKey(City3,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(Country3,on_delete=models.CASCADE,null=True,blank=True)
    plant=models.ForeignKey(Plants3,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.time)





class Country4(models.Model):
    country_id=models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.country_name)

class City4(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country4, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city_name', 'country')

    def __str__(self):
        return str(self.city_name)

class CountryCity4(models.Model):
    city = models.ForeignKey(City4, on_delete=models.CASCADE)
    country = models.ForeignKey(Country4, on_delete=models.CASCADE)

class news4(models.Model):
    img=models.ImageField(upload_to='photos')
    time=models.DateField()
    case=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    city=models.ForeignKey(City4,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(Country4,on_delete=models.CASCADE,null=True,blank=True)
    plant=models.CharField(max_length=100)

    def __str__(self):
        return str(self.time)


class MyMedia(models.Model):
    image = models.ImageField(upload_to='photos')
