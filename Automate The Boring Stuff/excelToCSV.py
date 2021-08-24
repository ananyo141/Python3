# Convert Excel files (.xlsx) to Comma-separated files (.csv)
import tkinter.filedialog, csv, os, sys
from ModuleImporter import module_importer
openpyxl = module_importer('openpyxl', 'openpyxl')

def main():
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory specified")
    directory = os.path.normpath(directory)

    # Open all the excel files in the user-given directory
    saveDir = os.path.join(directory, 'CSV')
    os.makedirs(saveDir, exist_ok = True)
    for file in os.listdir(directory):
        if os.path.splitext(file)[1] != '.xlsx':
            continue
        # For every sheet of excel spreadsheet, create a new csv file
        filepath = os.path.join(directory, file)
        xlfile = openpyxl.load_workbook(filepath)
        for sheetname in xlfile.sheetnames:
            sheet = xlfile[sheetname]
            sheetSaveName = os.path.join(saveDir, os.path.splitext(os.path.basename(filepath))[0] + '_' + sheetname + '.csv')
            with open(sheetSaveName, 'w', newline = '') as csvfile:
                # Create save file
                csvWriter = csv.writer(csvfile)
                # Write the contents of excel spreadsheet in csv
                for rowNum in range(1, sheet.max_row + 1):
                    writeBuffer = []                    # initialize buffer for each row
                    for colNum in range(1, sheet.max_column + 1):
                        writeBuffer.append(sheet.cell(row = rowNum, column = colNum).value)
                    csvWriter.writerow(writeBuffer)     # write the buffer for the current row
            print(f'Converted file {sheetSaveName}')

if __name__ == '__main__':
    main()
