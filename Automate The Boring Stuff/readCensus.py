#!python3
# Read the census from the 'censuspopdata.xlsx' file and write the data as a 
# dictionary and save as census2010.py
import pprint
from ModuleImporter import module_importer
pyxl = module_importer('openpyxl', 'openpyxl')

def main():
    # Open the excel workbook and get the census sheet
    print("Opening file")
    workbook = pyxl.load_workbook('./censuspopdata.xlsx')
    sheet = workbook['Population by Census Tract']
    countyData = {}
    print("Calculating data")
    # Fill in countyData with each county's population and tracts.
    for row in range(2, sheet.max_row + 1):
        state = sheet.cell(row = row, column = 2).value
        county = sheet.cell(row = row, column = 3).value
        pop = sheet.cell(row = row, column = 4).value

        # fill in the countyData data-structure
        # Making sure state exists
        countyData.setdefault(state, {})
        # making sure population and tract exists
        countyData[state].setdefault(county, {'pop': 0, 'tract': 0})

        # calculating the data
        countyData[state][county]['tract'] += 1
        countyData[state][county]['pop'] += int(pop)

    # saving the data in file
    print("Creating file")
    saveFile = open('./census2010.py', 'w')
    saveFile.write('allData = ' + pprint.pformat(countyData))
    saveFile.close()
    print('Done')

if __name__ == '__main__':
    main()