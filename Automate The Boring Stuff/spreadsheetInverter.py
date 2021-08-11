# This program invert the cells of a spreadsheet - the columns become the rows and rows the columns
import tkinter.filedialog, os
from ModuleImporter import module_importer
openpyxl = module_importer('openpyxl', 'openpyxl')

def main():
    # take the file
    filename = tkinter.filedialog.askopenfilename(filetypes = [('Excel Spreadsheet', '*.xlsx')])
    if not filename:
        print("No files chosen")
        os._exit(1)

    workbookSrc = openpyxl.load_workbook(filename)
    worksheetSrc = workbookSrc.active
    # create a new workbook
    workbookDst = openpyxl.Workbook()
    worksheetDst = workbookDst.active
    print("Inverting workbook")
    worksheetDst.title = worksheetSrc.title
    # traverse each cell and place the new cells in their designated position in the new file
    for row in range(1, worksheetSrc.max_row + 1):
        for column in range(1, worksheetSrc.max_column + 1):
            try:
                worksheetDst.cell(row = column, column = row).value = worksheetSrc.cell(row = row, column = column).value
            except:
                continue
    # save the file
    saveFile = os.path.dirname(filename) + os.sep + 'invertedSheet.xlsx'
    workbookDst.save(saveFile)
    print("Saved successfully saved in " + saveFile)

if __name__ == '__main__':
    main()