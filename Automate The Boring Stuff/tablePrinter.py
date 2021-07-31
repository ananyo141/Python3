# Write a table printer that takes a list of list as argument and prints the nested lists as columns
# that are left, centre and right justified resp. Also takes an optional argument that specifies the
# title of the table, by default title should be 'TABLE'.

import sys

def tablePrinter(nestedList,title):
    '''(list of list of str)--> NoneType
    Takes a nestedList as argument and prints as columns that are right
    justified.
    '''
    
    # Remove any blank column that will create error
    columnCount = 1
    for list in nestedList:
        if len(list) < 1:
            print(f"Blank column detected at column {columnCount}")
            nestedList.remove(list)
        columnCount += 1

    # Exit if there is nothing in the list, doesn't sys.exit(), returns none and continues execution.
    if len(nestedList) < 1:
        print("No data given.")
        return

    # Finds the column width to specially format the specific column
    columnWidth=[]
    for i in range(len(nestedList)):
        bestChoice = None
        for string in nestedList[i]:
            if bestChoice == None:
                bestChoice = len(string)
            if len(string) > bestChoice:
                bestChoice = len(string)

        columnWidth.append(bestChoice)

    # Prints the title
    print(title.center(sum(columnWidth),'*'))
    
    # Prints the table according to spacing from column width
    for i in range(len(nestedList[0])):
        for j in range(len(nestedList)):
            print(nestedList[j][i].rjust(columnWidth[j]),end=' ')
        print('\n')


def main():
    title=input("Enter the title of the table: ")
    totalList=[]
    columnNum=1
    column=input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
    if column.lower() == 'no':
            print(f"You stopped at column: {columnNum-1}")
        
    elif column.lower() != 'yes' and column.lower() != 'no':
        print(f"You entered wrong choice. Operation stopped at: {columnNum-1}")
        column = input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
        while column.lower()!= 'yes' and column.lower()!='no':
            print(f"You entered wrong choice. Operation stopped at: {columnNum-1}")
            column = input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
    while column.lower() == 'yes':

        addToColumn = input("Enter column elements(done to exit): ")
        columnContents = []
        while addToColumn.lower() != 'done':
            columnContents.append(addToColumn)
            addToColumn = input("Enter column elements(done to exit): ")
            
        totalList.append(columnContents)
        columnNum += 1
        column = input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
        if column.lower()=='yes':
            continue
        if column.lower() == 'no':
            print(f"You stopped at column: {columnNum-1}")
            break
        else:
            print(f"You entered wrong choice. Operation stopped at column: {columnNum-1}")
            
            column = input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
            while column.lower()!= 'yes' or column.lower!='no':
                column = input(f"Start column {columnNum}? \n('Yes' to continue, 'No' to exit): ")
            continue
    
    if len(title)<1 and len(totalList)!=0:
        title="TABLE"

    if len(title) < 1 and len(totalList) < 1:
        sys.exit("NULL INPUT")

    if len(totalList)<1:
        print(title.center(len(title)+10,'*'))
        sys.exit("Nothing else to print")

    tablePrinter(totalList,title)

if __name__=='__main__':
    main()
