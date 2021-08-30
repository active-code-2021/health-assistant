from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(process.env.IAMAUTHENTIATOR_WOTSON)
assistant = AssistantV2(
    version='{version}',
    authenticator=authenticator
)

assistant.set_service_url(process.env.URL_TRIAL_WOTSON)

assistant.set_disable_ssl_verification(True)