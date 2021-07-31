# There is a mistake at the document https://docs.google.com/spreadsheets/u/0/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/htmlview
# by Al, figure out the row at which he made it.
import ezsheets

def main():
    try:
        spreadsheet = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    except Exception as e:
        print(str(e))
        quit()

    sheet = spreadsheet[0]
    # download the three columns for minimum requests-hangup
    firstCol = sheet.getColumn(1)
    secondCol = sheet.getColumn(2)
    thirdCol = sheet.getColumn(3)
    # check the calculation row-wise
    for i in range(1, sheet.rowCount + 1):
        firstVal = int(firstCol[i])
        secondVal = int(secondCol[i])
        thirdVal = int(thirdCol[i])
        # print out the row number where the mistake lies
        if firstVal * secondVal != thirdVal:
            print('The mistake is at row: ' + str(i + 1))
            print('Given Answer = ' + str(thirdVal))
            print('Correct Answer = ' + str(firstVal * secondVal))
            break

if __name__ == '__main__':
    main()