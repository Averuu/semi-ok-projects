
import pyperclip as ppc
import tkinter as tk
#--------------------Логика--------
def checkDot(arr):#ставит заглавные буквы 
	if ord(arr[0]) > 1071:
		arr[0] = chr(ord(str(arr[0])) - 32)
	
	for i in range(len(arr) - 2):
		if arr[i] in bigSymbolsAfter:
			letter = ord(str(arr[i + 2]))
			if letter > 1071:
				arr[i + 2] = chr(letter - 32)
		if arr[i]  == "\n":
			letter = ord(str(arr[i + 1]))
			if letter > 1071:
				arr[i + 1] = chr(letter - 32)
	return arr
	
	
	
	
def checkSpace(arr):
	for i in range(len(arr) - 2):
		if arr[i] in symbolsWithSpaces:
			if arr[i + 1] != " ":
				arr.insert(i + 1, " ")
	return arr



	
def fakeSymbol(arr):
	for i in range(len(arr)):
		try:
			if arr[i:i + 5] == dot1 or arr[i:i + 5] == dot2:
				arr[i - 1] = "."
				for j in range(5):
					arr.pop(i)#убирает 5 символов
					
			elif arr[i:i + 4] == tr1 or arr[i:i + 4] == tr2:
				arr[i - 1] = "-"
				for j in range(4):
					arr.pop(i)
					
			elif arr[i:i + 7] == zp1 or arr[i:i + 7] == zp2:
				arr[i - 1] = ","
				for j in range(7):
					arr.pop(i)

		except IndexError:
			continue
	return arr
#arr[i:i+5]


dot1 = [i for i in "Точка"]# ["Т","о","ч","к","а"]
dot2 = [i for i in "точка"]
tr1 = [i for i in "Тире"]
tr2 = [i for i in "тире"]
zp1 = [i for i in "Запятая"]
zp2 = [i for i in "запятая"]
symbolsWithSpaces = [".", ",", "!", "?", "-"]
bigSymbolsAfter = [".", "!", "?"]


#-----------Логика2------------------
rawtext = ""
def makeText(event):
	
	#rawtxt = ppc.paste()
	rawtext = window.clipboard_get()
	arr = []
	for i in rawtext:
		arr.append(i)
	if ord(arr[0]) > 1071:
		arr[0] = chr(ord(str(arr[0])) - 32)
	arr = fakeSymbol(arr)
	arr = checkSpace(arr)
	arr = checkDot(arr)
	
	text_out.insert("1.0", "".join(arr))
	rawtext = "".join(arr)
	ppc.copy(rawtext)
def copyText(event):
	ppc.copy(rawtext)
	print(rawtext)
#-------------Окно--------------------

window = tk.Tk()
#Label, Button, Entry, Text, Frame
"""
"red"
"orange"
"yellow"
"green"
"blue"
"purple"
"""
label = tk.Label(
    text="На текстовое поле выведется\nисправленный текст",
    foreground="black",  # Set the text color to white
    background="#b4dbff", # Set the background color to black
    width=50,
    height=3
)
button = tk.Button(
    text="Вставить и форматировать текст",
    width=25,
    height=3,
    bg="blue",
    fg="yellow",
)
button.bind("<Button-1>", makeText)
button2 = tk.Button(
    text="Копировать текст",
    width=25,
    height=3,
    bg="blue",
    fg="yellow",
)
button.bind("<Button-2>", copyText)
"""
Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()
"""
text_in = tk.Text(height=9)
text_out = tk.Text(height=14)

label.pack()
#text_in.pack()
button.pack()
text_out.pack()
button2.pack()

window.mainloop()
