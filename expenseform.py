import os
import tkinter as tk
from tkinter import filedialog
from images2pdf import *
from pypdf import PdfWriter

root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
if path is None or len(path) == 0: exit()

# Get list of files
filepaths_images = []
filepaths_pdfs = []
filepath_expenseform = ""
for f in os.listdir(path):
	f = os.path.join(path, f)
	if os.path.isfile(f):
		if len(filepath_expenseform) or os.path.splitext(f)[1].lower() != ".pdf": raise Exception("Expected a single pdf file on the top level of the provided directory (the expense form)")
		filepath_expenseform = f
	#
	else:
		directory = f
		for f in os.listdir(directory):
			f = os.path.join(directory, f)
			ext = os.path.splitext(f)[1].lower()
			if ext in (".jpg", ".png"): filepaths_images.append(f)
			elif ext == ".pdf": filepaths_pdfs.append(f)
			else: print("Warning: unexpected file extension \"", f, "\"")
		#
	#
#
if len(filepath_expenseform) == 0: raise Exception("Expense form not found")
if len(filepaths_images) == 0 and len(filepaths_pdfs) == 0: raise Exception("No receipts found in folder")

# Convert image-format receipts to pdf
path_converted_receipts = os.path.join(path, "tmp_converted_receipts.pdf")
images2pdf(filepaths_images, path_converted_receipts)

# Merge all involved pdfs
merger = PdfWriter()
pdfs = [filepath_expenseform] + filepaths_pdfs + [path_converted_receipts]
for pdf in pdfs: merger.append(pdf)
merger.write(os.path.splitext(filepath_expenseform)[0] + "_merged.pdf")
merger.close()

# Remove tmp file
os.remove(path_converted_receipts)

