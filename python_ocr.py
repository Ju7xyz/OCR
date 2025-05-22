from PIL import Image

im_file = "ocr_python/data/page_01.jpg"

im = Image.open(im_file)
im.save("ocr_python/temp/page_01.jpg")