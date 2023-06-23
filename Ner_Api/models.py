from django.db import models

# Create your models here.
class NerEntity(models.Model):
    text = models.TextField()
    label = models.CharField(max_length=100)



class PersonEntity(models.Model):
    person = models.CharField(max_length=255)
    description = models.TextField()
    summarized_description = models.TextField()
    class Meta:
        managed = False 
        db_table = 'person_entity'


    def __str__(self):
        return f"{self.person} - {self.description} - {self.summarized_description}"


class MoneyEntity(models.Model):
    money = models.CharField(max_length=250)
    description = models.TextField()
    summarized_description = models.TextField()
    class Meta:
        managed = False 
        db_table = 'money_entity'
   

    def __str__(self):
        return f"{self.money} - {self.description} - {self.summarized_description}"
    

class LocEntity(models.Model):
    loc = models.CharField(max_length=250)
    description = models.TextField()
    summarized_description = models.TextField()
    class Meta:
        managed = False 
        db_table = 'loc_entity'


    def __str__(self):
        return f"{self.loc} - {self.description} - {self.summarized_description}"
    
class GpeEntity(models.Model):
    gpe = models.CharField(max_length=250)
    description = models.TextField()
    summarized_description = models.TextField()
    class Meta:
        managed = False 
        db_table = 'gpe_entity'

    def __str__(self):
        return f"{self.gpe} - {self.description} - {self.summarized_description}"

class OrgEntity(models.Model):
    org = models.CharField(max_length=250)
    description = models.TextField()
    summarized_description = models.TextField()
    class Meta:
        managed = False 
        db_table = 'org_entity'
    
    def __str__(self):
        return f"{self.org} - {self.description} - {self.summarized_description}"
