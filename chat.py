import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(process.env.IAMAUTHENTIATOR_WOTSON)
assistant = AssistantV2(
    version='2018-11-08',
    authenticator = authenticator
)
url = process.env.URL_WOTSON
assistant.set_service_url(url)
session_id = assistant.create_session(
    assistant_id=process.env.ASSISTANT_ID_WOTSON
).get_result()["session_id"]



response = assistant.message(
    assistant_id=process.env.ASSISTANT_ID_WOTSON,
    session_id=session_id,
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))