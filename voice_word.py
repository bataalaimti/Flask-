from gtts import gTTS

def txt_voice(text):
    my_obj = gTTS(text=text, lang='en', slow=False)
    my_obj.save(f'static\Voice\{text}.mp3')
