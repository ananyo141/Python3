# Remove the csv headers from a directory.
import tkinter.filedialog, csv, os, sys, shutil, time

def main():
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory chosen.")

    # take the current time
    start = time.time()
    # make directory path windows-like incase of windows
    directory = os.path.normpath(directory)
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] != '.csv':
            continue
        print('Found csv: %s...' % (filename))

        # Open the read and write files for reading and writing
        filename = os.path.join(directory, filename)
        savefilename = os.path.splitext(filename)[0] + '_temp.csv'
        with open(filename, 'r') as readFile, open(savefilename, 'w', newline = '') as writeFile:
            reader = csv.DictReader(readFile)
            writer = csv.writer(writeFile)
            for row in reader:
                writer.writerow([row['NAICS'], row['NAICS Description'], row['Item'],
                                row['Tax Status'], row['Employer Status'], row['2012 Revenue'], 
                                row['2011 Revenue'], row['2010 Revenue'], row['2012 Coefficient of Variation'], 
                                row['2011 Coefficient of Variation'], row['2010 Coefficient of Variation']])
        
        # rename to replace the file
        shutil.move(savefilename, filename)

    end = time.time()
    print('Operation finished in %d second(s)' % (end - start))

if __name__ == '__main__':
    main()
