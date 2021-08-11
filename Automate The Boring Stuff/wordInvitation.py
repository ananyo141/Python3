# This program creates invitations for people names written in guests text file
import tkinter.filedialog, sys, os
from ModuleImporter import module_importer
docx = module_importer('docx', 'python-docx')

def main():
    # Take the guests file from the user
    guestsFile = tkinter.filedialog.askopenfilename(filetypes = [('Text Files', '*.txt')])
    if not guestsFile:
        sys.exit('No guests file selected')
    heading = input('Enter the heading of the invitation: ')
    date = input('Enter the date of event: ')
    with open(guestsFile, 'r') as openedGuestsFile:
        guests = openedGuestsFile.readlines()

    # Open up an invitation docx
    # Create a docx file
    docfile = docx.Document()
    # For each guest, write an invitation
    for guest in guests:
        docfile.add_heading(heading, 0)
        docfile.add_paragraph().add_run('It would be a pleasure to have the company of').italic = True
        docfile.paragraphs[1].runs[0].add_break()
        docfile.add_paragraph().add_run(guest).small_caps = True
        docfile.paragraphs[2].runs[0].add_break()
        docfile.add_paragraph('at 11010 Memory Lane on the Evening of')
        docfile.add_paragraph(date)
        docfile.add_paragraph().add_run("At 7 o'clock").add_break(docx.enum.text.WD_BREAK.PAGE)
    docfile.save(os.path.join(os.path.dirname(guestsFile), 'Guest Invitations.docx'))

if __name__ == '__main__':
    main()
