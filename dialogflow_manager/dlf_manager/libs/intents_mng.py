from django.conf import settings
from google.protobuf.json_format import MessageToDict
from dlf_manager.models import Intents
import dialogflow_v2 as dialogflow

project_id = settings.DLF_PROJECT_ID
language_code = settings.DLF_LANG

client = dialogflow.IntentsClient()
parent = client.project_agent_path(project_id)


def dlf_and_localdb_sync():
    for page in client.list_intents(parent).pages:
        for raw_element in page:
            element = MessageToDict(raw_element)
            intents_db = Intents(
                name=element.get('name'),
                display_name=element.get('displayName'),
                priority=element.get('priority')
            )
            intents_db.save()
