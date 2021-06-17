#https://cloud.google.com/text-to-speech/docs/reference/libraries#client-libraries-install-python
import os
from google.cloud import texttospeech
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='Demo.json'

client = texttospeech.TextToSpeechClient()

message=input("ป้อนข้อความของคุณ :")
synthesis_input = texttospeech.types.SynthesisInput(text=message)
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('result.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Export result.mp3 Complete')
