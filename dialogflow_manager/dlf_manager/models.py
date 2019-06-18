from django.db import models


# Create your models here.
class Intents(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255, null=False)
    priority = models.IntegerField(null=True)
    # input_context_names = models.ForeignKey(
    #     'InputContexts',
    #     on_delete=models.CASCADE
    # )
    # parameters
    # output_contexts


# class InputContexts(models.Model):
#     name = models.CharField(max_length=255, primary_key=True)
