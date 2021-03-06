# Find all the photo folders in a given directory
import tkinter.filedialog, os, sys, logging
from ModuleImporter import module_importer
PIL = module_importer('PIL', 'Pillow')
from PIL import Image

# filename = 'photoFolders.log'
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def main():
    supportedFormats = ['.png', '.jpg', '.gif', '.bmp']
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory chosen")

    directory = os.path.normpath(directory)

    # Crawl the directory   
    for directory, subdir, filenames in os.walk(directory):
        photoFiles = 0
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() in supportedFormats:
    # For each directory, find the number of photos (height and width > 500px)
                try:
                    image = Image.open(os.path.join(directory, filename))
                except:
                    logging.error("Couldn't open file", os.path.join(directory, filename))
                    continue
                imWidth, imHeight = image.size
                if imWidth > 500 and imHeight > 500:
                    photoFiles += 1

    # If number of photos is more than half of the files in the directory,
        if photoFiles > 15 and photoFiles > len(filenames) / 2:
            print(directory, "is a Photo Folder")


if __name__ == '__main__':
    main()
