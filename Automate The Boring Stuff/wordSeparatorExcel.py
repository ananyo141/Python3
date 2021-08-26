# Separates the words of a different text files in a spreadsheet and insert them per row per file.
import tkinter.filedialog, os
from ModuleImporter import module_importer
openpyxl = module_importer('openpyxl', 'openpyxl')

CELL_COLUMN_WIDTH = 12
TITLE_COLUMN_WIDTH = 24

def main():
    # take files input
    filenames = tkinter.filedialog.askopenfilenames(filetypes = [('Text Files', '*.txt')])
    if not filenames:
        print("No files selected")
        os._exit(1)
    # for every file write the contents in a row, each cell containing a word
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    print("Creating spreadsheet...")
    worksheet.title = 'File Contents'
    worksheet.column_dimensions['A'].width = 25     # make the title column wide
    for i in range(len(filenames)):
        words = open(filenames[i], 'r').read().split(' ')
        titleCell = worksheet.cell(row = i + 1, column = 1)
        titleCell.value = os.path.basename(filenames[i]).rstrip('.txt')
        titleCell.font = openpyxl.styles.Font(name = 'Verdana', bold = True, italic = True)
        for j in range(len(words)):
            worksheet.cell(row = i + 1, column = j + 2).value = words[j]
            worksheet.column_dimensions[openpyxl.utils.get_column_letter(j + 2)].width = CELL_COLUMN_WIDTH

    # save the spreadsheet
    save_file = os.path.dirname(filenames[0]) + os.sep + 'ContentSpreadsheet.xlsx'
    workbook.save(save_file)
    print("Spreadsheet saved as " + save_file)


if __name__ == '__main__':
    main()