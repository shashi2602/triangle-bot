from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
import requests
from requests.auth import HTTPBasicAuth
from gradio_client import Client
# from appwritedb import add_history,fetch_user_history


app = Flask(__name__)

TWILIO_AUTH_SID = 'auth_id'
TWILIO_AUTH_TOKEN = 'auth_token'

GOOGLE_GEMINI_KEY = 'googlekey'

genai.configure(api_key=GOOGLE_GEMINI_KEY)


def gen_ai_google_response(content,type):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if type == 'url':
        prompt = f"Please summarize the content found at the following URL into a concise paragraph that captures the main points. The summary should be clear and easy to understand and. Here is the URL:{content}"
    if type == 'text':
        prompt = f"Please summarize the following text into a concise paragraph that captures the main points. The summary should be clear and easy to understand. Here is the text:{content}"
    if type == 'tweet':
        prompt = f"Please summarize the following text into a concise, engaging tweet. The tweet should be within 280 characters and include relevant hashtags and emojis if applicable. Here is the text:{content}"
    if type == "ask":
        prompt =content
    response = model.generate_content(prompt)
    return response.text

def audio_to_text(twilio_audio):
    audio_url = requests.get(twilio_audio, auth=HTTPBasicAuth(TWILIO_AUTH_SID, TWILIO_AUTH_TOKEN)).url
    client = Client("https://openai-whisper.hf.space/")
    result = client.predict(
                    audio_url,	
                    "transcribe",	
                    api_name="/predict"
        )
    return result


@app.route('/bot', methods=['POST'])  # This is the route that receives messages from Twilio
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    profil_name = request.values.get('ProfileName', '').lower()
    # user_id = request.values.get('AccountSid', '').lower()
    response = MessagingResponse()
    message = response.message()
    responded = False 
    
    # Check if the incoming message contains the word "summarize"
    if 'summarize' in incoming_msg:
        summary_content = incoming_msg[14:]
        summary_type = incoming_msg[0:14].split(' ')[1]
        summary = gen_ai_google_response(summary_content, summary_type)
        message.body(summary)
        # add_history(summary_type, incoming_msg, summary, user_id)
        responded = True
    
    # Check if the message is an audio message
    if request.values.get("MessageType") == "audio":
        audio_text = audio_to_text(request.values.get("MediaUrl0"))
        message.body(str(audio_text))
        # add_history("Audio Note", "audio_text", audio_text, user_id)
        responded = True
    
    # Check if the message contains the word "tweet"
    if "tweet" in incoming_msg:
       tweet = gen_ai_google_response(incoming_msg[5:],"tweet")       
       message.body(str(tweet))
    #    add_history("tweet", incoming_msg, tweet, user_id)
       responded = True
    
    # Check if the message contains the word "ask"
    if "ask" in incoming_msg:
        answer = gen_ai_google_response(incoming_msg[4:],"ask")
        message.body(str(answer))
        # add_history("ask", incoming_msg, answer, user_id)
        responded = True

    if not responded:
        message.body(f"*Hi {profil_name}!*\n\n *Welcome to the Triangl WhatsApp Bot!* 🤖\n\nI'm here to help you with several tasks. Here's what you can do: \n\n 1. **Summarize Text** 📝\n   - Send: `summarize text <your text here>`\n\n 2. **Summarize URL Content** 🌐\n  s - Send: `summarize url <your URL here>`\n\n 3. **Create a Tweet** 🐦\n   -Send: `tweet <your text here>` \n\n -Create a audio note 🎤 \n   -record audio and send it will exract the text \n\n -Ask AI \n  ask any thing to ai with command `ask prompt`" )
    
    # Return the response message in TwiML format
    return str(response)

if __name__ == '__main__':
    app.run(port=4000)