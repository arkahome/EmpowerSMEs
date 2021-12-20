from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class PIModel(models.Model):
    choices_y_n = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    model_pk = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #models.CharField(max_length=200, primary_key=True)
    model_name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    tags = models.CharField(max_length=300)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=150, null=True)
    insourcing_or_not = models.CharField(max_length=6,choices=choices_y_n)
    insourcing_code = models.CharField(max_length=20, null=True, blank=True)
    deployed_yes_or_no = models.CharField(max_length=6,choices=choices_y_n, null=True)
    deployed_on = models.DateField(null=True)
    total_savings_deployed =  models.FloatField(null=True)
    sub_model_pk = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name

class PISubModel(models.Model):
    model_pk = models.ForeignKey(PIModel, on_delete=models.CASCADE)
    sub_model_pk = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_model_name =  models.CharField(max_length=300)
    sub_model_description = models.TextField(max_length=1000)
    code_type = models.CharField(max_length=10)
    code = models.TextField(max_length=10000)
    opportunity_size = models.FloatField(null=True)
    insourcing_overlap_perc = models.FloatField(null=True)
    insourcing_comm_saved = models.FloatField(null=True)
    insourcing_incremental_savings = models.FloatField(null=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=150, null=True)
    select_as_main_model = models.BooleanField()

    def __str__(self):
        return self.sub_model_name
