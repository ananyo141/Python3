# Create custom invitation for guests in the guests.txt file with background image
# specified by the user from the internet
import tkinter.filedialog, requests, sys, os
from PIL import Image, ImageDraw, ImageFont

def main():
    textFile = tkinter.filedialog.askopenfilename(title = 'Enter guests file', 
               filetypes = [('Text File', '*.txt')])
    if not textFile:
        sys.exit("No file chosen")
    imageLink = input("Enter the link of image: ")
    if not imageLink:
        sys.exit("No image link given")
    saveDir = os.path.join(os.path.dirname(textFile), 'Invitations')
    os.makedirs(saveDir, exist_ok=True)
    # Open the guests text file and read contents
    guests = open(textFile).read().split('\n')

    # Download the file, keep it as temporary file
    try:
        image = requests.get(imageLink)
        image.raise_for_status()
    except:
        sys.exit("Unable to download image")

    with open('_temp.png', 'wb') as tempFile:
        for chunk in image.iter_content(1000000):
            tempFile.write(chunk)    

    # Create a new image with the image as background, keep it as template (adjust it's opacity)
    with Image.open('_temp.png') as template:
        template = template.resize((600, 300))
        for guest in guests:
        # For every guest, copy a template and write the name of the guest
            baseImage = template.copy()
            monotypeFont = ImageFont.truetype('MTCORSVA.TTF', 35)
            draw = ImageDraw.Draw(baseImage)
            draw.text((baseImage.width // 3 , baseImage.height // 3), guest, fill = 'gray', font = monotypeFont)
            # Save the file
            baseImage.save(os.path.join(saveDir, guest + '.png'))

    os.unlink('_temp.png')


if __name__ == '__main__':
    main()
