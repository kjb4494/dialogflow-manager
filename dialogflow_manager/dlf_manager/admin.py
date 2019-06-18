from django.contrib import admin
from dlf_manager.models import Intents, InputContexts, OutputContexts, Parameters

# Register your models here.
admin.site.register(Intents)
admin.site.register(InputContexts)
admin.site.register(OutputContexts)
admin.site.register(Parameters)
