
import json
import os
import string
from pypdf import PdfMerger


def import_file(import_file_name):

    return_data = []

    if import_file_name == None:
        return None, "import_file_name is empty:{}".format(import_file_name)

    try:
        import_file = open(import_file_name, mode='r')
    except:
        return None, "open() error:{}".format(import_file_name)

    try:
        import_data = import_file.readlines()
    except:
        return None, "readlines() error:{}".format(import_file_name)

    for data in import_data:
        return_data.append(data.strip())

    return return_data


def merge_pdfs(direct_path) -> bool:
    files = os.listdir(direct_path)
    ext = ('.pdf')
    pdfs = []
    for file in files:
        if file.endswith(ext):
            pdfs.append(file)
        else:
            continue

    handler = PdfMerger()

    direct_path = "workspace/"
    maerge_sequence = import_file(direct_path+'outline.txt')
    if not len(maerge_sequence) == len(pdfs):
        print("WARMING the file number in outline.txt is not the same with in the direct")

    try:
        print("read", maerge_sequence)
        for pdf in maerge_sequence:
            print("read {}".format(pdf))
            handler.append(direct_path+pdf)

        name = direct_path+"result.pdf"
        handler.write(name)
        handler.close()
        return True

    except:
        print("Merge PDFs Failed")
        return False


if __name__ == '__main__':
    merge_pdfs("merge_pdfs")
