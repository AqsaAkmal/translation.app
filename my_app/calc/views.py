from googletrans import Translator
from django.shortcuts import render
from gtts import gTTS
from django.http import HttpResponse
import mimetypes
import os
import time
import random

def home(request):
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'submit':
                text = request.POST.get("text")
                language = request.POST.get("language")
                print(language)
                if text and language:
                    translator = Translator()
                    result = translator.translate(text, dest=language)
                    translated_text = result.text
                else:
                    translated_text = "Translation not available"

                return render(request, 'home.html', {'translation': translated_text,'textvalue':text})

            elif action == 'listen':
                translated_text = request.POST.get("txtTranslated","")
                print(request.POST.get("txtTranslated",""))
                print(request.POST)
                text = request.POST.get("text")
                if translated_text:
                    try:
                     tts = gTTS(translated_text)
                     tts.save("my_app/static/temp_audio.mp3")
                    except Exception as e:
                      print(f"Error generating audio: {e}")
                    random_value=random.randint(1, 10000)
                    return render(request, 'home.html',{'audio_generated': True,'random_value':random_value,'textvalue':text,'translation': translated_text})
                

    return render(request, 'home.html')

