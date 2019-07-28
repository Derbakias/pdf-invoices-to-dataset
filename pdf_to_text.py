import glob  # finds all the pathnames
from tika import parser  # extracts text from pdf

# pdf files location as a list
pdf_files_list = (glob.glob("/home/dell/PycharmProjects/invoices to dataset/*.pdf"))


# loop through pdf files
# uses negative index just for the data to be in a correct order
for pdf_file in pdf_files_list[::-1]:

    # full text from pdf
    raw = parser.from_file(pdf_file)
    rawlist_full = (raw['content'])

    # search for keyword 'Total' and 'Summary' to start and finish the list slicing
    idx_total = int(rawlist_full.index('Total') + 7)
    idx_summary = int(rawlist_full.index('Summary') - 2)

    # save cleaned text to variable
    rawlist_cleaned = (raw['content'][idx_total:idx_summary])

    print()
    print(rawlist_cleaned)
