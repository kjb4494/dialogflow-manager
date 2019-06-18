from django.conf import settings
from google.protobuf.json_format import MessageToDict
import dialogflow_v2 as dialogflow

project_id = settings.DLF_PROJECT_ID
language_code = settings.DLF_LANG

client = dialogflow.IntentsClient()
parent = client.project_agent_path(project_id)


def get_all_intents():
    for page in client.list_intents(parent).pages:
        for element in page:
            print(MessageToDict(element))
            print("- " * 40)
