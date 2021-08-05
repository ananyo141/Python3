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

import importlib, tkinter.filedialog, logging, sys, os
logging.basicConfig(filename = './pdfConverter.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%S %p', filemode = 'w')

# import third - party modules safely
fpdf = module_importer('fpdf', 'fpdf2')
from fpdf import FPDF
requests = module_importer('requests', 'requests')

# Using inheritance to use custom header and footer
class PDF(FPDF):
    # Defining custom-header
    def header(self):
        # font 
        self.set_font('times', 'B', 17)
        # set text-color
        self.set_text_color(220, 50, 50)
        # position title in the center
        self.cell(0, 10, ln = True, align = 'C')
        # line break
        self.ln(10)

    # Defining custom-footer
    def footer(self):
        # set position of footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # set font color grey
        self.set_font_color(169, 169, 169)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align = 'C')

def main():
    # TODO: Take a list of filenames to convert
    textFiles = tkinter.filedialog.askopenfilenames(filetypes = [('Text Files', '*.txt')])
    # TODO: Input the title
    title = input('Enter a title of the pdfs: ')
    header = input('Enter the header text of the files: ')
    # TODO: Ask the user to input the url of an image for logo (header)
    imgUrl = input('Enter a valid url of an image you want to use as a logo: ')
    if not imgUrl:
        sys.exit('Image url not specified')

    # TODO: Build pdf for every text file
    saveDir = os.dirname(textFiles[0]) + os.sep + 'PDFs'
    os.mkdir(saveDir) 
    for filename in textFiles:
        pdf = PDF('P', 'mm', 'A4')
        pdf.alias_nb_pages()    # get total page numbers
        pdf.add_page()
        pdf.set_font('times', 'BIU', 16)
        with open(filename, 'rb') as file:
            content = file.read().decode('latin-1')
            pdf.multi_cell(0, 14, content, align = 'J')
        pdf.save(os.path.join(saveDir, os.path.splitext(filename)[1]))
    # TODO: Font color:-> black
    # TODO: Styles:-> font-family, font-color, font-style, fill-color
    # TODO: Metadata:-> title, author
    # TODO: Link


if __name__ == '__main__':
    main()
