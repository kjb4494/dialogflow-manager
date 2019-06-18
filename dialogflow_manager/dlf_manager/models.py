from django.db import models


# Create your models here.
class Intents(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255, null=False)
    priority = models.IntegerField(null=False)


class InputContexts(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255, null=False)
    input_context = models.ForeignKey(Intents, on_delete=models.CASCADE, null=False, related_name='input_context')


class OutputContexts(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255, null=False)
    lifespan_count = models.IntegerField(null=True)
    output_context = models.ForeignKey(Intents, on_delete=models.CASCADE, null=False, related_name='output_context')


class Parameters(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255, null=False)
    value = models.CharField(max_length=255, null=True)
    default_value = models.CharField(max_length=255, null=True)
    entity_type_display_name = models.CharField(max_length=255, null=True)
    parameters = models.ForeignKey(Intents, on_delete=models.CASCADE, null=False, related_name='parameters')
