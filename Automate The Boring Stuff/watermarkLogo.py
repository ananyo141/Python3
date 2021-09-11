# Batch process the images in the selected directory to resize images more than 300
# pixels (either height or width) and scale down the other dimension proportionally,
# then add a logo to bottom right corner

import tkinter.filedialog, logging, sys
from pathlib import Path
from ModuleImporter import module_importer
PIL = module_importer('PIL', 'Pillow')
from PIL import Image

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')  # filename = 'watermarkLogo.log', filemode = 'w'
logging.disable(logging.CRITICAL)

SQUARE_FIT_SIZE = 300

def calculate_resized_dim(width, height, max_size):
    ''' Calculate the resized image height and width and 
    shrink proportionally if it exceeds max_size and return integer values'''
    ratio = height / width
    if max(height, width) > max_size:
        if height > width:
            height = max_size
            width = (1 / ratio) * height
        if width > height:
            width = max_size
            height = ratio * width

        return int(width), int(height)
    return int(width), int(height)


def main():
    supportedFormats = ['.jpg', '.png', '.gif', '.bmp']
    logoFilePath = tkinter.filedialog.askopenfilename(title = "Enter logo image", 
                filetypes = [('JPEG', '*.jpg'), ('Portable network graphics', '*.png'), ('GIF', '*gif'), ('BMP', '*.bmp')])
    if not logoFilePath:
        sys.exit("Logo not entered")

    logoImage = Image.open(logoFilePath)
    # shrink the logo image too
    logoWidth, logoHeight = calculate_resized_dim(logoImage.width, logoImage.height, SQUARE_FIT_SIZE // 4)
    logoImage = logoImage.resize((logoWidth, logoHeight));                          logging.info(f"{logoWidth = }, {logoHeight = }")

    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory chosen")
    directory = Path(directory);                                                    logging.info(f"{logoFilePath = }, {directory = }")
    saveDir = directory / 'WithLogo';                                               logging.info(f"{saveDir = }")
    saveDir.mkdir(exist_ok = True)
    # Scan the directory for images of extension JPG, PNG, GIF, BMP 
    for item in directory.glob('*.*'):
        if item.is_file() and item.suffix.lower() in supportedFormats:
            if item.name == Path(logoFilePath).name:
                continue
            image = Image.open(item);                                               logging.info(f"{item = }")
            width, height = image.size;                                             logging.info(f"{width = }, {height = }")
            # If dimension is more than 300px, scale down the image (both preserving proportion)
            new_width, new_height = calculate_resized_dim(width, height, SQUARE_FIT_SIZE); logging.info(f"{new_width = }, {new_height = }")

            # Paste the logo image to the bottom corner
            print("Resizing image %s" % item.name)
            image = image.resize((new_width, new_height))
            image.paste(logoImage, (new_width - logoWidth, new_height - logoHeight), logoImage)
            # Save the image to separate directory
            image.save(saveDir / item.name);                                        logging.info(f"{(saveDir / item.name) = }")
            print("Added logo to %s" % item.name)

if __name__ == '__main__':
    main()
