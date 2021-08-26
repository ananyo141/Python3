# Reverse the wordSeparatorExcel program
import tkinter.filedialog, os
from ModuleImporter import module_importer
openpyxl = module_importer('openpyxl', 'openpyxl')

def main():
    # take the spreadsheet
    xlfilename = tkinter.filedialog.askopenfilename(filetypes = [('Excel Spreadsheet', '*.xlsx')])
    workbook = openpyxl.load_workbook(xlfilename)
    sheet = workbook.active
    directory = os.path.dirname(xlfilename) + os.sep + 'Extracted Text Files'
    os.mkdir(directory)
    print("Extracting files")
    # make file for each row
    for i in range(1, sheet.max_row + 1):
        textfile = open(directory + os.sep + sheet.cell(row = i, column = 1).value + '.txt', 'w')
        # write s of each row into text file separated by space and save
        for j in range(2, sheet.max_column + 1):
            try:
                textfile.write(sheet.cell(row = i, column = j).value + ' ')
            except TypeError:
                break
        textfile.close()
    print("Files saved at " + directory)

if __name__ == '__main__':
    main()
