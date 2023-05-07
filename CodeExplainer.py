from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import openai
from tkinter.ttk import *
from PIL import ImageTk

openai.api_key = 'используйте свой api ключ' #Мы не можем предоставить вам свой api ключ, на хакатоне мы продемонстрируем, как это работает

def select_text():

    selected_text = code_edit.get("sel.first", "sel.last")
    callback(selected_text)
def select_text2():

    selected_text = code_edit.get("sel.first", "sel.last")
    callback2(selected_text)

def callback(selected_text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"напиши комментарий по коду:\n {selected_text}",
    temperature=0.5,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )
    tokens = response.choices[0].text.strip().split('\n')
    text = ' '.join(tokens)
    txt_edit.insert(tk.END, f"\n\n{text}")

def clear():
    txt_edit.delete('1.0',END)
    
def callback2(selected_text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"напиши подробный комментарий по коду:\n {selected_text}",
    temperature=0.5,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )
    tokens = response.choices[0].text.strip().split('\n')
    text = ' '.join(tokens)
    txt_edit.insert(tk.END, f"\n\n{text}")

def open_file():
    
    filepath = askopenfilename(
        filetypes=[("py-файл", "*.py"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r", encoding='utf-8') as input_file:
        text = input_file.read()
        code_edit.delete('1.0',END)
        code_edit.insert(tk.END, text)
        CtNL(text)
    window.title(f"ГАС CodeExplainer - {filepath}")
        
def CtNL(license):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"напиши комментарии к коду:\n {license}",
    temperature=0.5,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )
  tokens = response.choices[0].text.strip().split('\n')
  text = ' '.join(tokens)
  txt_edit.insert(tk.END, text)
 
def save_file():
    
    filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("py-файлы", "*.py"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding='utf-8') as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"ГАС CodeExplainer - {filepath}")

window = tk.Tk()
window.title("ГАС CodeExplainer")
window.rowconfigure(0, minsize=1920, weight=1)
window.columnconfigure(1, minsize=1080, weight=1)

image = ImageTk.PhotoImage(file="trash_bin_icon-icons.com_67981.png")

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=1,bg='grey40')
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(fr_buttons, text="Сохранить как...", command=save_file)
select_button = tk.Button(fr_buttons, text="Комментарий по выделению", command=select_text)
select_button2 = tk.Button(fr_buttons, text="подробный комментарий по выделению", command=select_text2)
clear_button = tk.Button(fr_buttons, command=clear,image = image)
code_edit = tk.Text(window)
txt_edit = tk.Text(window)
scrollbar = tk.Scrollbar(window, command=code_edit.yview)
scrollbar_2 = tk.Scrollbar(window, command=code_edit.xview)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5,pady = 5)
select_button.grid(row= 3,column = 0, sticky = 'ew', padx = 5, pady=5)
select_button2.grid(row= 4,column = 0, sticky = 'ew', padx = 5, pady=5)
clear_button.grid(row= 5,column = 0, sticky = 'ew', padx = 5, pady=589)

code_edit.configure(yscrollcommand=scrollbar.set)
code_edit.configure(xscrollcommand=scrollbar_2.set)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nes")
code_edit.grid(row=0, column=1, sticky="nsew")

txt_edit.config(fg='snow',bg = 'gray25')
code_edit.config(fg='snow',bg = 'gray25')

btn_open.config(bg='grey27',fg='snow')
btn_save.config(bg='grey27',fg='snow')
select_button.config(bg='grey27',fg='snow')
select_button2.config(bg='grey27',fg='snow')
clear_button.config(bg='grey27', fg='snow')

window['bg'] = 'grey40'

scrollbar.grid(row=0, column=1, sticky="ns")
scrollbar_2.grid(row=1, column=0,sticky ='we')

window.mainloop()