# Insert blank rows in a excel spreadsheet at a given row
import tkinter.filedialog, openpyxl, sys, os

def main():
    print("Enter the file you want to add rows to:")
    filename = tkinter.filedialog.askopenfilename(filetypes=[('Excel Spreadsheet', '*.xlsx')])
    if not filename:
        sys.exit("No file selected")
    
    try:
        rowNum = int(input("Enter the row number where you want to insert gaps: "))
        gapNum = int(input("Enter the number of gaps: "))
    except:
        sys.exit("Integer value expected")

    print("Opening Workbook")
    workbook = openpyxl.load_workbook(filename)
    sheetSrc = workbook.active
    print("Creating a new workbook")
    newWorkbook = openpyxl.Workbook()
    sheetDst = newWorkbook.active

    print("Copying the data and adding gaps")
    # write the first rowNum number of rows
    for row in range (1, rowNum):
        for column in range(1, sheetSrc.max_column + 1):
            try:
                sheetDst.cell(row = row, column = column).value = sheetSrc.cell(row = row, column = column).value
            except:
                continue

    # write the gapped rows
    for row in range(rowNum, sheetSrc.max_row + 1):
        for column in range(1, sheetSrc.max_column + 1):
            try:
                sheetDst.cell(row = row + gapNum, column = column).value = sheetSrc.cell(row = row, column = column).value
            except:
                continue
        
    saveDir = filename[:filename.rfind(os.sep) + 1]
    newWorkbook.save(saveDir + 'gappedWorkbook.xlsx')
    print("Output workbook is saved at " + saveDir)


if __name__ == '__main__':
    main()