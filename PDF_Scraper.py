# a simple PDF scraper using pyPDF2 and tkinter for the open/save functions.
# opens up a file and outputs the scrape of every page on a new line in a CSV.
# poorly commented... I'll work on that

import PyPDF2
from PyPDF2 import PdfFileMerger
import csv
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
import os

root = Tk()
root.withdraw()

# Popup to ask where to save the CSV and what to call the CSV
file_save = filedialog.asksaveasfilename(defaultextension='.csv')

# print(file_save)

file_path = filedialog.askopenfilename()

with open(file_save, 'w', newline='') as csvfile:

    pdfFileObj = open(file_path, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    
    # For debugging
    print(pdfReader.numPages)

    # can obviously be whatever you want. This was applicable to my situation.
    fieldnames = ['Testpack', 'PDF_Data']
    CSVOutput = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Scrub from each page in the range and output to new line in CSV
    for x in range(pages):
        pageObj = pdfReader.getPage(x)

        print(pdfReader.resolvedObjects)
        
        CSVOutput.writerow({'Testpack': pdfFileObj, 'PDF_Data': pageObj.extractText()})

    # pageObj = pdfReader.getPage(0)
    # print(pageObj.extractText())
root.deiconify()
text = tk.Text(root, heigh=2, width=30)
text.pack()
text.insert(tk.END, "Data scrape complete.")
root.mainloop()
