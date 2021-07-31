# This script extracts the data from a google form spreadsheet.
import ezsheets, os

def count_responses(firstColumn):
    '''(list) --> int
    Return the number of non-empty rows in the given list of row values. Ignores spaces.
    '''
    responseCount = 0
    for value in firstColumn:
        if not value:
            continue
        responseCount += 1

    return responseCount

def main(): 
    # Take the spreadsheet id from the user
    spreadsheetId = input('Enter the google-form generated spreadsheet Id: ')
    try:
        spreadsheet = ezsheets.Spreadsheet(spreadsheetId)
    except Exception as exc:
        print(str(exc))
        os._exit(1)

    sheet = spreadsheet[0]

    # Take the column headers whose data needs to be extracted
    columns_to_be_scraped = []
    print("Enter column headers to extract ('done' to exit): ")
    i = 1
    while True:
        answer = input(str(i) + '. ')
        if answer.lower() == 'done':
            break
        columns_to_be_scraped.append(answer.lower())
        i += 1

    columnData = {}
    # Extract the data for each column 
    # dictionary with the keys as the column header and values as the list of column values
    headerRow = sheet.getRow(1)     # download the row for efficiency
    for i, columnHeader in enumerate(headerRow):
        if columnHeader.lower() in columns_to_be_scraped:
            columnData[columnHeader] = sheet.getColumn(i + 1) # this includes the column header
        if len(columns_to_be_scraped) == len(columnData):
            break

    print('Generating file...')
    # Write the data in a text file
    file = open('./FormAnalysis.txt', mode = 'w')
    file.write((sheet.title).center(100) + '\n')
    file.write(('(' + str(count_responses(sheet.getRow(1))) + ' Responses)').rjust(100) + '\n')
    for column in columnData:
        file.write((' ' + column + ' ').center(25, '*') + '\n')
        for i, data in enumerate(columnData[column]):
            if i == 0 or not data:
                continue  # skip the column header or empty cells
            file.write(data + '\n')
        file.write('\n')

    file.close()
    print(f'File saved in {os.getcwd()}')

if __name__ == '__main__':
    main()