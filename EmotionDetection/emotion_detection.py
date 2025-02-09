import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header) 
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:

        # Extracting emotion label and score from the response
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Create a dictionary containing sentiment analysis results
        result = {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score
                }

        # Extract emotion with highest score and add to result
        dominant_emotion = max(result, key=lambda item: result[item])
        result['dominant_emotion'] = dominant_emotion

    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        result = {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }


     # Send a POST request to the API with the text and headers
    return result # Return the response text from the API