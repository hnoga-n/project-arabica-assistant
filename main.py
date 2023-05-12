from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
import time
import openai
import sys
import speech_recognition as sr
# from sqlalchemy.util import ABC
from sqlalchemy.util import classproperty
from abc import ABC, abstractmethod

# import arabica

root = tk.Tk()

root.geometry('500x480+550+100')
root.title('Arabica')
root.config(bg='black')
root.resizable(False,False)

image = Image.open("logo.png")
image = image.resize((60, 60)) 
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
label.place(x=15,y=3)

logo_font = font.Font(family="Arial", size= 20, weight="bold")
label_text = tk.Label(root, text="Arabica Assistant", bg='black', fg='white', font= logo_font)
label_text.place(x=130,y=18)

frame = tk.Frame(root, width=500, height=350, bg='black')
frame.place(x=0,y=70)
frame.propagate(False)

text_font = font.Font(family="Arial", size=13)
text=tk.Text(frame, bg='white', fg='black' , font=text_font)
text.pack(side='left')


def enter_key_pressed(event):
    if event.keysym == 'Return':
        #returnAsk()
        Ask()

textfield = tk.Entry(root, width=30,font="Arial 14")
textfield.bind('<Key>',enter_key_pressed)
textfield.place(x=10,y=430,height=35)

def split_string(string):
    # Tách chuỗi thành các từ
    words = string.split()
    # Tạo danh sách các chuỗi con
    substrings = []
    substring = ''
    # Thêm các từ vào chuỗi con
    for word in words:
        if len(substring + ' ' + word) <= 50:
            if ( '!' in word or '?' in word or ':' in word):
                substring += ' ' + word
                substrings.append(substring.strip())
                substring = ''
            else :
                substring += ' ' + word
        else:
            substrings.append(substring.strip())
            substring = word
    # Thêm chuỗi con cuối cùng
    if substring:
        substrings.append(substring.strip())

    return substrings

def split_string1(string):
    strs = string.split("\n")
    return strs

#Hàm truyền vào một chuỗi để in ra câu trả lời
def Answer(a):
    text.tag_configure("left", justify='left')
    text.insert(tk.END,"Arabica:\n","left")
    openai.api_key = "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"
    # Gọi API để tạo câu trả lời từ model
    for response in openai.Completion.create(
        engine="text-davinci-003", # Loại model ngôn ngữ
        prompt=a,
        max_tokens=2048,
        n=1, # Số lượng kết quả trả về
        stop=None, # Điều kiện dừng để kết thúc câu trả lời
        temperature=0.5, # Độ đa dạng của kết quả (từ 0 đến 1)
        stream=True
    ):
        text.insert(tk.END,response.choices[0].text,"left")
        text.update_idletasks()
        text.see(tk.END)
    text.config(state=DISABLED)

def LowerAnswer(a):
    text.tag_configure("left", justify='left')
    text.insert(tk.END,"Arabica:\n","left")
    s = split_string1(a)
    for vd in s:
        strs=split_string(vd)
        for i in strs:
            text.insert(tk.END,i + "\n","left")
    text.insert(tk.END,"\n", "left")

    text.see(tk.END)
    text.config(state=DISABLED)

# Hàm xử lý sự kiện khi nút "Enter" được nhấn
def Ask():
    text.config(state=NORMAL)
    text.tag_configure("right", justify='right')
    content = textfield.get()
    text.insert(tk.END,"\nYou:\n", "right")
    s = split_string(content)
    for i in s:
        text.insert(tk.END, i + "\n", "right")
    text.insert(tk.END, "\n", "right")
    text.see(tk.END)
    main(content)
    textfield.delete(0, tk.END)

def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: ")
        audio = r.listen(source)
    try:
        text_vi = r.recognize_google(audio, language="vi")
        return text_vi
        text_en = r.recognize_google(audio, language="en")
        return text_en
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def microphone():
    text.config(state=NORMAL)
    text.tag_configure("left", justify='left')
    text.insert(tk.END,"Arabica:\nListening . . .","left")
    text.insert(tk.END,"\n", "left")
    text.see(tk.END)
    text.config(state=DISABLED)
    response = listening()
    text.config(state=NORMAL)
    text.tag_configure("right", justify='right')
    text.insert(tk.END,"\nYou:\n" + response, "right")
    text.insert(tk.END, "\n", "right")
    text.see(tk.END)
    main(response)

# Tạo nút "Enter"
button_right = tk.Button(root, text="Enter", command=Ask, height=2 , width=7)
button_right.place(x=430,y=430)
# Tạo nút "Micro"
button_mic = tk.Button(root, text="Mic", command=microphone, height=2 , width=7)
button_mic.place(x=360,y=430)

def main(content):
    a = content
    if(a==""):
        LowerAnswer("How can I help you ?")
    elif 'time' in a.lower():
        import datetime
        LowerAnswer("Let me check the time for you...\nThe current time is " + \
        datetime.datetime.now().strftime('%H:%M'))
    else: 
        Answer(a)
root.mainloop()
