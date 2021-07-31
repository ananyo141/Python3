import tkinter.filedialog
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image = '/mnt/0FBF0B0B0FBF0B0B/betaCode/fpdf2/fox_face.png'

filename = tkinter.filedialog.askopenfilename(filetypes = [('Text Files', '*.txt')])
with open(filename, mode = 'rb') as file:
    text = file.read().decode('latin-1')

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('helvetica', 'B', 12)
pdf.set_text_color(220,12,50)
pdf.set_fill_color(14, 155, 10)
pdf.multi_cell(0, 5, text, align = 'J', fill=True)

pdf.output('./mypdf.pdf')
