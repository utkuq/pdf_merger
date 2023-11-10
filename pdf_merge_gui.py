import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PyPDF2 import PdfMerger

root = tk.Tk()
root.title('PDF Merger')
root.geometry("300x100")
root.eval('tk::PlaceWindow . center')

arr = []
def fileSelect():
    filetypes = (("PDF Files", "*.pdf"), ("All Files", "*.*"))
    filenames = fd.askopenfilenames(title="Open Files", initialdir="/", filetypes=filetypes)
    arr = [i for i in filenames]
    merge(arr)

def merge(arr):
    merger = PdfMerger()

    for pdf in arr:
        merger.append(pdf)

    with open("merged.pdf", "wb") as output:
        merger.write(output)
    messagebox.showinfo("Info","Merging Completed")

      
btn1 = tk.Button(master=root, text="Select Files & Merge", command=fileSelect)
btn1.pack(padx=10, pady=40)
root.mainloop()