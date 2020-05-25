import requests
from googletrans import Translator

def translate_wrapper(sentence,target):
    """
    Translate sentence to target language using googletrans library which is a Google Translate API wrapper,
    call this function when you don't have Google Translate API credentials
    :param sentence: sentence to translate
    :param target: target language value can be: ar,fr,en,de,ru,zh,ja,it,... visit for more language https://cloud.google.com/translate/docs/languages
    :return translated sentence
    """
    translator = Translator()
    
    try:
        # translate the 'text' column
        response = translator.translate(sentence, dest=target)

    except Exception as e: # mean Google restrict IP address
        response = "Probably Google has banned your client IP addres"+str(e)
        return response
    
    return response.text

def translate(sentence,target,api_key):
    """
    Translate sentence to target language using googletrans library which a Google Translate API wrapper
    :param sentence: sentence to translate
    :param target: target language value can be: ar,fr,en,de,ru,zh,ja,it,... visit for more language https://cloud.google.com/translate/docs/languages
    :param api_key: credential for Google Translator API https://console.cloud.google.com/apis/credentials? 
    :return translated sentence
    """
    #translate without using googletrans wrapper library
    URL = "https://translation.googleapis.com/language/translate/v2?target="+target+"&key="+api_key+"&q="+sentence
    # sending get request and saving the response as response object 
    r = requests.get(url = URL)

    if r.status_code == 200:
        # extracting data in json format 
        data = r.json()
        return data['data']['translations'][0]['translatedText']

if __name__ == "__main__":
    print(translate_wrapper("This is a test sentence","fr"))
    print(translate("This is a test sentence","fr","myGoogleTranslateAPICredential"))