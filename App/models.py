from django.db import models

# Create your models here.
# Parameters: Start Date, End Date, Principal, Interest (optional).
class Model(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    principal = models.IntegerField()
    interest = models.FloatField(null=True)
    
    def grand_Total(self):
        return  self.principal + self.interest

    def _str_(self):
        return self.interest