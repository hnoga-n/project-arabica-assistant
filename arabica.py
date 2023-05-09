import pyttsx3
import speech_recognition as sr
import datetime
import openai
import sys

def arabica_init():
    arabica=pyttsx3.init()
    voice=arabica.getProperty('voices')
    arabica.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    return arabica

def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: ")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="en")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def speak(audio):
    arabica=arabica_init()
    print("Arabica: "+audio)
    arabica.say(audio)
    arabica.runAndWait()
def generate_chatbot_response(input_text):
    # Thiết lập API key của bạn
    openai.api_key = "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"

    
    # Gọi API để tạo câu trả lời từ mô hình
    for response in openai.Completion.create(
        engine="text-davinci-003", # Loại mô hình ngôn ngữ
        prompt=input_text,
        max_tokens=2048,
        n=1, # Số lượng kết quả trả về
        stop=None, # Điều kiện dừng để kết thúc câu trả lời
        temperature=0.5, # Độ đa dạng của kết quả (từ 0 đến 1)
        stream=True
    ):
        sys.stdout.write(response.choices[0].text)
        sys.stdout.flush()
    # Lấy câu trả lời từ kết quả trả về
    """ answer = response['choices'][0]['text']
    return answer """
""" try:
    while True:
        # Sử dụng hàm để tạo trả lời từ trợ lý ảo
        input_text = input("You: ")
        # input_text = listening()
        if("bye" in input_text):
            break
        generate_chatbot_response(input_text)

        # In câu trả lời ra màn hình
        # speak(response)
        # print(response)
except:
    pass """

