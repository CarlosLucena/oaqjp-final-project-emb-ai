import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str):
    data = f'{{"raw_document": {{"text": \"{text_to_analyze}\"}} }}'
    response = requests.post(URL, data=data,  headers=Header)
    json = response.json()
    emotion_dic = json["emotionPredictions"][0]['emotion']
    emotion_dic["dominant_emotion"] = max(emotion_dic, key=emotion_dic.get)
    return emotion_dic
