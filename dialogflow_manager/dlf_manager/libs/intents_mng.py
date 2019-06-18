from django.conf import settings
from google.protobuf.json_format import MessageToDict
from dlf_manager.models import Intents, InputContexts, OutputContexts, Parameters
import dialogflow_v2 as dialogflow

project_id = settings.DLF_PROJECT_ID
language_code = settings.DLF_LANG

client = dialogflow.IntentsClient()
parent = client.project_agent_path(project_id)

contexts_path = 'projects/' + project_id + '/agent/sessions/-/contexts/'


def dlf_and_localdb_sync():
    Intents.objects.all().delete()
    for page in client.list_intents(parent).pages:
        for raw_element in page:
            element = MessageToDict(raw_element)
            intents_db = Intents(
                name=element.get('name'),
                display_name=element.get('displayName'),
                priority=element.get('priority')
            )
            intents_db.save()

            input_contexts_list = element.get('inputContextNames')
            if input_contexts_list is not None:
                for input_context in input_contexts_list:
                    input_contexts_db = InputContexts(
                        name=input_context,
                        display_name=input_context.replace(contexts_path, ''),
                        input_context=intents_db
                    )
                    input_contexts_db.save()

            output_contexts_list = element.get('outputContexts')
            if output_contexts_list is not None:
                for output_context in output_contexts_list:
                    output_contexts_db = OutputContexts(
                        name=output_context.get('name'),
                        display_name=output_context.get('name').replace(contexts_path, ''),
                        lifespan_count=output_context.get('lifespanCount'),
                        output_context=intents_db
                    )
                    output_contexts_db.save()

            params_list = element.get('parameters')
            if params_list is not None:
                for param in params_list:
                    params_db = Parameters(
                        name=param.get('name'),
                        display_name=param.get('displayName'),
                        value=param.get('value'),
                        default_value=param.get('defaultValue'),
                        entity_type_display_name=param.get('entityTypeDisplayName'),
                        parameters=intents_db
                    )
                    params_db.save()
