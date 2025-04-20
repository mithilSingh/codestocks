from tkinter import *

import PyPDF2
import PyPDF2 as pd
from  gtts import gTTS
from tkinter import filedialog
root2=Tk()
def get_the_value_of_save_location (a):
    save_location=filedialog.askdirectory()
    e2.insert(0,save_location)
def get_the_value_of_pdf_location (a):
    save_location = filedialog.askopenfilename(title="select the pdf file",filetypes=[("pdf file","*.pdf")])
    e.insert(0, save_location)
def convert():
    open_location=e.get()
    save_location=e2.get()
    name_of_file=name.get()
    file = open(open_location, "rb")
    reader = PyPDF2.PdfFileReader(file)
    newframe = Frame(root2, height=200,width=300)
    newframe.place(x=0, y=0)
    Label(newframe, text="please wait").place(x=120,y=80)
    root2.update()
    main_text=""


    for i in range(reader.numPages):
        page=reader.getPage(i)
        text=page.extractText()
        " ".join(text.split())
        main_text+=text
    converter=gTTS(main_text ,slow=False)
    converter.save(save_location+f"/{name_of_file}")
    newframe.destroy()
def main():
    global e,e2,name
    root=Frame(root2,height=200,width=300)
    root.place(x=30,y=0)
    Label(root, text="name of your audiobook").pack()
    name = Entry(root,width=23)
    name.pack()
    Label(root, text="pdf location").pack()

    f1 = Frame(root)
    f1.pack()


    e=Entry(f1)
    e.grid(column=0,row=0)

    open_button=Button(f1,text="pdf",command=lambda :get_the_value_of_pdf_location(e.get()))
    open_button.grid(column=1,row=0)

    Label(root, text="you want to save it in-").pack()

    f2 = Frame(root)
    f2.pack()

    e2= Entry(f2)
    e2.grid(column=0, row=0)

    save_button = Button(f2, text="save",command=lambda :get_the_value_of_save_location(e2.get()))
    save_button.grid(column=1, row=0)
    create=Button(root,text="create",command=convert)
    create.pack()
main()
root2.title("Audiobook")
root2.geometry("300x200")
root2.mainloop()
