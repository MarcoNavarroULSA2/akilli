from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json

key = "3a5bbd11190e4f098a09221cfb1d4b8c"
endpoint = "https://manr1.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()
def key_phrase_extraction_example(client, texto):

    try:
        documents = [texto]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            frases = []
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
                frases.append(phrase)
            
            frases_json = json.dumps(frases)
            print(frases_json)


            return frases_json
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
#key_phrase_extraction_example(client,texto)

