from PIL import Image

def images2pdf(filepaths, out):
	if len(filepaths) == 0: return
	pics = [Image.open(f) for f in filepaths]
	pics = [p.convert("RGB") for p in pics]
	pics[0].save(out, save_all=True, append_images=pics[1:])
	return
#

