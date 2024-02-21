import tkinter as tk
from tkinter import ttk

from tkinter import *

import base64
import pyperclip
from pdf2image import convert_from_path


# Eine PDF mit dem Namen "test.pdf" muss in den Ordner der Python-Datei gelegt werden.

# Store Pdf with convert_from_path function
images = convert_from_path('test.pdf',700,poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')

for i in range(len(images)):

    # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    i=i+1
# print(len(images))


output = []
for i in range(len(images)):
    with open('page'+ str(i) +'.jpg', "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        my_string = str(my_string[4:-2])
        pyperclip.copy(my_string)

        zwischenablage = pyperclip.paste()
        i = str(i +1)
        zwischenablage = "var imgData_" + i + " = 'data:image/jpeg;base64,/9j/" + zwischenablage[2:-1] + "';"
        output.append(zwischenablage)
# pyperclip.copy(str(output[2]))
print(i)






def covert_pdf_to_jpg_to_base64_and_copy_1():
    pyperclip.copy(str(output[0]))

def covert_pdf_to_jpg_to_base64_and_copy_2():
    pyperclip.copy(str(output[1]))

def covert_pdf_to_jpg_to_base64_and_copy_3():
    pyperclip.copy(str(output[2]))

def covert_pdf_to_jpg_to_base64_and_copy_4():
    pyperclip.copy(str(output[3]))

def covert_pdf_to_jpg_to_base64_and_copy_5():
    pyperclip.copy(str(output[4]))

def covert_pdf_to_jpg_to_base64_and_copy_6():
    pyperclip.copy(str(output[5]))

def covert_pdf_to_jpg_to_base64_and_copy_7():
    pyperclip.copy(str(output[6]))

def covert_pdf_to_jpg_to_base64_and_copy_8():
    pyperclip.copy(str(output[7]))

def covert_pdf_to_jpg_to_base64_and_copy_9():
    pyperclip.copy(str(output[8]))

def covert_pdf_to_jpg_to_base64_and_copy_10():
    pyperclip.copy(str(output[9]))



def covert_pdf_to_jpg_to_base64_and_copy_all():
    print(i)
    if i == "1":
        ausgabe = str(output[0])

    if i == "2":
        ausgabe = str(output[0]) + " " +  str(output[1])

    if i == "3":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2])

    if i == "4":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3])

    if i == "5":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4])

    if i == "6":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4]) + " " +  str(output[5])

    if i == "7":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4]) + " " +  str(output[5]) + " " +  str(output[6])

    if i == "8":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4]) + " " +  str(output[5]) + " " +  str(output[6]) + " " +  str(output[7])

    if i == "9":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4]) + " " +  str(output[5]) + " " +  str(output[6]) + " " +  str(output[7]) + " " +  str(output[8])

    if i == "10":
        ausgabe = str(output[0]) + " " +  str(output[1]) + " " +  str(output[2]) + " " +  str(output[3]) + " " +  str(output[4]) + " " +  str(output[5]) + " " +  str(output[6]) + " " +  str(output[7]) + " " +  str(output[8]) + " " +  str(output[9])




    pyperclip.copy(ausgabe)















root = tk.Tk()
root.title("Titel")
root.geometry("250x650")
root.minsize(width=250, height=650)
root.resizable(width=True, height=True)
root.attributes('-topmost', True)

style = ttk.Style()








button1 = ttk.Button(root, text = "1. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_1, style="big.TButton")
button1.pack()



button2 = ttk.Button(root, text = "2. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_2, style="big.TButton")
button3 = ttk.Button(root, text = "3. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_3, style="big.TButton")
button4 = ttk.Button(root, text = "4. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_4, style="big.TButton")
button5 = ttk.Button(root, text = "5. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_5, style="big.TButton")
button6 = ttk.Button(root, text = "6. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_6, style="big.TButton")
button7 = ttk.Button(root, text = "7. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_7, style="big.TButton")
button8 = ttk.Button(root, text = "8. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_8, style="big.TButton")
button9 = ttk.Button(root, text = "9. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_9, style="big.TButton")
button10_10 = ttk.Button(root, text = "10. Seite", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_10, style="big.TButton")
button10 = ttk.Button(root, text = "Alle Seiten", padding=15, command=covert_pdf_to_jpg_to_base64_and_copy_all, style="big.TButton")


if i >= "2":
    button2.pack()

if i >= "3":
    button3.pack()

if i >= "4":
    button4.pack()

if i >= "5":
    button5.pack()

if i >= "6":
    button6.pack()

if i >= "7":
    button7.pack()

if i >= "8":
    button8.pack()

if i >= "9":
    button9.pack()

if i >= "10":
    button10_10.pack()

button10.pack()





style.configure('big.TButton', font=(None, 20))








root.mainloop()

