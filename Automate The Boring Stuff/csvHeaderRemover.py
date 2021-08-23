# Remove the csv headers from a directory.
import tkinter.filedialog, csv, os, sys, shutil, time

def main():
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory chosen.")
    # Incase of windows: make directory path windows-like
    directory = os.path.normpath(directory)

    # take the current time
    start = time.time()
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] != '.csv':
            continue
        print('Found csv: %s...' % (filename))

        # Open the read and write files for reading and writing
        filename = os.path.join(directory, filename)
        savefilename = os.path.splitext(filename)[0] + '_temp.csv'
        # get the table headers
        with open(filename) as readFile:
            headerList = []
            headReader = csv.reader(readFile)
            for header in list(headReader)[0]:
                headerList.append(header)
        # write the file taking the first row as the header
        with open(filename, 'r') as readFile, open(savefilename, 'w', newline = '') as writeFile:
            reader = csv.DictReader(readFile)
            writer = csv.writer(writeFile)
            for row in reader:
                writeList = []
                for header in headerList:
                    writeList.append(row[header])
                writer.writerow(writeList)
        # rename to replace the file
        shutil.move(savefilename, filename)

    # Record endtime
    end = time.time()
    print('Operation finished in %.4f second(s)' % (end - start))


if __name__ == '__main__':
    main()
