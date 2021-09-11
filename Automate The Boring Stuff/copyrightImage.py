# Copyright the images in the given directory with a custom copyright text

import tkinter.filedialog, datetime, sys, os, ModuleImporter
PIL = ModuleImporter.module_importer('PIL', 'Pillow')
from PIL import Image, ImageDraw, ImageFont

def getDate() -> str:
    ''' Return the current date formatted like 01-Jan-2001 '''
    now = datetime.datetime.now()
    return now.strftime('%d-%b-%Y')

def main():
    supportedFormats = ['.jpg', '.png', '.gif', '.bmp']

    # Choose directory to put watermark on photos
    directory = tkinter.filedialog.askdirectory(title = 'Enter photo folder')
    if not directory:
        sys.exit("No directory chosen")
    directory = os.path.normpath(directory)
    saveDir = os.path.join(directory, 'Watermarked')

    # Enter the watermark text
    watermarkText = input("Enter the watermark text: ")
    customFont = ImageFont.truetype('comic.ttf', 25)
    
    # Search the directory for photos 
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file) and os.path.splitext(file)[1] in supportedFormats:
            os.makedirs(saveDir, exist_ok = True)
            print("Applying watermark %s..." % filename)
            image = Image.open(file)
            draw = ImageDraw.Draw(image)
            # Apply the watermark
            draw.text((10, 10), watermarkText, fill='gray', font = customFont)
            draw.text((image.width - 200, image.height - 60), getDate(), fill= 'black', font = customFont)
            # Save in new folder
            imageSaveName = os.path.join(saveDir, filename)
            image.save(imageSaveName)
            print("Saving file %s" % imageSaveName)

    print("Done.")

if __name__ == '__main__':
    main()
