import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
if path is None or len(path) == 0: exit()

filepaths = []
for f in os.listdir(path):
	f = os.path.join(path, f)
	if not os.path.isfile(f): continue
	if os.path.splitext(f)[1].lower() == ".jpg" or os.path.splitext(f)[1].lower() == ".png":
		filepaths.append(f)
	#
#
if len(filepaths) == 0:
	raise Exception("No images found in folder")
	exit()
#

def images2pdf(filepaths, out):
	if len(filepaths) == 0: return
	pics = [Image.open(f) for f in filepaths]
	pics = [p.convert("RGB") for p in pics]
	pics[0].save(out, save_all=True, append_images=pics[1:])
	return
#

images2pdf(filepaths, os.path.join(path, "out.pdf"))

