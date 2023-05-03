from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
import time

# from sqlalchemy.util import ABC
from sqlalchemy.util import classproperty
from abc import ABC, abstractmethod

import arabicas

root = tk.Tk()

root.geometry('350x480+460+80')
root.title('Arabicas')
root.config(bg='black')
root.resizable(False,False)

image = Image.open("logo.png")
image = image.resize((35, 35))  # Điều chỉnh kích thước hình ảnh
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
#label.pack(anchor="nw", padx=15, pady=15)
label.place(x=15,y=15)

logo_font = font.Font(family="Times New Roman", size= 15, weight="bold")
label_text = tk.Label(root, text="Arabicas Assistant", bg='black', fg='white', font= logo_font)
label_text.place(x=70,y=25)

frame = tk.Frame(root, width=350, height=350, bg='black')
frame.place(x=0,y=70)
frame.propagate(False)


#centerFrame.place(relx=0.5,rely=0.5,anchor='center')
# scrollbar=tk.Scrollbar(frame)
# scrollbar.pack(side='right')

text=tk.Text(frame, bg='white', fg='black')
text.pack(side='left')


def enter_key_pressed(event):
    if event.keysym == 'Return':
        #returnAsk()
        Ask()

textfield = tk.Entry(root, width=42)
textfield.bind('<Key>',enter_key_pressed)
textfield.place(x=20,y=430)

def split_string(string):
    # Tách chuỗi thành các từ
    words = string.split()

    # Tạo danh sách các chuỗi con
    substrings = []
    substring = ''

    # Thêm các từ vào chuỗi con
    for word in words:
        if len(substring + ' ' + word) <= 30:
            if ('.' in word or '!' in word or '?' in word or ':' in word):
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
    text.insert(tk.END,"Arabicas:\n","left")
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
    text.insert(tk.END,"You:\n", "right")
    s = split_string(content)
    for i in s:
        text.insert(tk.END, i + "\n", "right")

    text.insert(tk.END, "\n", "right")
    text.see(tk.END)
    main(content)
    textfield.delete(0, tk.END)


# Tạo nút "Enter"
button_right = tk.Button(root, text="Enter", command=Ask)
button_right.place(x=290,y=430)

def hello():
    txt = "Hi! I'm Arabicas. How can I help you?"
    Answer(txt)
def main(content):
    tempt = 1
    while tempt!=0:
        a = content
        print("Me:",a)
        # a = listening()
        if("bye" in a):
            Answer("See you again!")
            tempt=1
        elif(("Hi" in a) | ("hi" in a)):
            hello()
            tempt=1
        else: 
            response = arabicas.generate_chatbot_response(a)
            # In câu trả lời ra màn hình
            Answer(response)
            print(response)
            tempt=1
        tempt=0
        # arabicas.speak(response)
hello()
root.mainloop()
