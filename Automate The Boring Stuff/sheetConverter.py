# Use google-spreadsheet to convert spreadsheets into other formats
import tkinter.filedialog, sys, os
from ModuleImporter import module_importer
ezsheets = module_importer('ezsheets', 'ezsheets')
pyip = module_importer('pyinputplus', 'pyinputplus')

def main():
    toConvert = tkinter.filedialog.askopenfilename(filetypes = [('Spreadsheet', '*.xlsx')])
    if not toConvert:
        sys.exit('File not selected')

    # upload the file
    try:
        print(f'Uploading file {os.path.basename(toConvert)}...')
        spreadsheet = ezsheets.upload(toConvert)
    except Exception as exc:
        sys.exit(str(exc))
    # take the file extension
    extension = pyip.inputMenu(['PDF', 'CSV', 'HTML', 'ODS', 'TSV'], prompt = 'Which extension you want to convert?\n', numbered = True)
    saveDir = tkinter.filedialog.askdirectory()
    if not saveDir:
        sys.exit('No save directory chosen')

    # download as the given format
    if extension.lower() == 'pdf':
        spreadsheet.downloadAsPDF(saveDir + os.sep + 'converted.pdf')
    elif extension.lower() == 'csv':
        spreadsheet.downloadAsCSV(saveDir + os.sep + 'converted.csv')
    elif extension.lower() == 'html':
        spreadsheet.downloadAsHTML(saveDir + os.sep + 'converted.html')
    elif extension.lower() == 'ods':
        spreadsheet.downloadAsODS(saveDir + os.sep + 'converted.ods')
    elif extension.lower() == 'tsv':
        spreadsheet.downloadAsTSV(saveDir + os.sep + 'converted.tsv')
    else:
        print('Unexprected format')
    print('Converting...')
    print(f'File saved at: {saveDir}')

    # delete the file after download
    spreadsheet.delete(permanent = True)

if __name__ == '__main__':
    main()
