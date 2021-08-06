#! python3
# This script converts text files into pdfs.
def module_importer(module_name, package_name):
    '''(str, str) -> ModuleType
    Read the module name as a string and try to import it normally,
    failing which tries to download required package and return the module.
    '''
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        print('Resolving dependencies...')
        print(f'Required Module: {package_name}')
        try:
            os.system('pip install ' + package_name)
            return importlib.import_module(module_name)
        except Exception as e:
            sys.exit(str(e))

def image_downloader(url: str) -> str:
    '''Takes the url of an image as argument and downloads the image, saves it to current directory 
    and returns it's path.
    '''
    image = requests.get(url);                                                 logging.warning(f'{url = }'); logging.critical(f'{image.status_code = }')
    try:
        image.raise_for_status()   
    except Exception as e:
        sys.exit(str(e))

    saveFilename = os.path.join(os.getcwd(), '_temp.jpg');                     logging.warning(f'{saveFilename = }')
    with open(saveFilename, 'wb') as saveFile:
        for chunk in image.iter_content(1000000):
            saveFile.write(chunk)

    return saveFilename

def random_color():
    '''(NoneType) -> int
    Return a random color between 0 to 255
    '''
    return random.randint(0, 255)

import importlib, tkinter.filedialog, random, logging, sys, os
# filename = './pdfConverter.log'
logging.basicConfig(level = logging.WARNING, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%S %p', filemode = 'w')
logging.disable(logging.CRITICAL)
logging.critical('*** Had to use elevated log levels due to conflicting logging from FPDF module ***')

            # Import third - party modules safely #
fpdf = module_importer('fpdf', 'fpdf2')
from fpdf import FPDF
requests = module_importer('requests', 'requests')

                    # Global Variables #
title = input('Enter title for the pdfs: ');                                   logging.warning(f'{title = }')
header = input('Enter the header text of the files: ');                        logging.warning(f'{header = }')
# Ask the user to input the url of an image for logo (header)
imgUrl = input('Enter a valid url of an image you want to use as a logo: ')
if not imgUrl:
    sys.exit('Image url not specified')
try:
    image_path = image_downloader(imgUrl)
except Exception as e:
    sys.exit(str(e))

            # Using inheritance to use custom header and footer #
class PDF(FPDF):
    # Defining custom-header
    def header(self):
        self.image(image_path, 10, 8, 25) # set the logo
        self.set_font('times', 'BI', 16) # font 
        self.set_text_color(random_color(), random_color(), random_color())  # set text-color
        self.cell(0, 10, header, ln = True, align = 'R') # position header in the right
        self.ln(9)  # line break

    # Defining custom-footer
    def footer(self):
        self.set_y(-15)  # set position of footer
        self.set_font('helvetica', 'I', 8) # set font
        self.set_text_color(169, 169, 169) # set font color grey
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align = 'C') # page number

def main():
    # Take a list of filenames to convert
    textFiles = tkinter.filedialog.askopenfilenames(filetypes = [('Text Files', '*.txt')])
    if not textFiles:
        sys.exit('No files chosen')     
    logging.warning(f'{textFiles = }')

    # Build pdf for every text file
    print('Building the pdfs...')
    saveDir = os.path.dirname(textFiles[0]) + os.sep + 'PDFs';                 logging.warning(f'{saveDir = }')
    os.makedirs(saveDir, exist_ok = True) 
    for filename in textFiles:
        pdf = PDF('P', 'mm', 'A4')  # pdf layout
        pdf.alias_nb_pages() # get total page numbers
        pdf.add_page()

        # set title at the first page
        pdf.set_font('helvetica', 'BU', 14)
        pdf.set_text_color(random_color(), random_color(), random_color())
        pdf.set_fill_color(random_color(), random_color(), random_color())
        pdf.cell(0, 15, title, ln = True, border = True, align = 'C', fill = True)
        pdf.ln(5)

        # write rest of content
        pdf.set_font('times', '', 16)
        pdf.set_title(title) # metadata
        pdf.set_author('pdfConverter-Python') # metadata
        pdf.set_text_color(10, 10, 10) # Font color:-> black-ish
        with open(filename, 'rb') as file:
            content = file.read().decode('latin-1')
            pdf.multi_cell(0, 9, content, align = 'J')
        saveName = saveDir + os.sep + os.path.basename(filename).rstrip('.txt') + '.pdf'
        pdf.output(saveName);                                                  logging.critical(f'{saveName = }')
        print(f'Created pdf: {os.path.basename(saveName)}')

    print('Deleting temporary files...')    
    os.unlink(image_path) # delete the temp image
    print(f'The output pdfs are created at {saveDir}')


if __name__ == '__main__':
    main()
