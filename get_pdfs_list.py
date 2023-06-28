
import os


def get_pdfs_list(direct_path):
    files = os.listdir(direct_path)
    ext = ('.pdf')
    pdfs = []
    for file in files:
        if file.endswith(ext):
            pdfs.append(file)
        else:
            continue
    return pdfs


def export_file(file_path, data):
    if not data:
        print("Error, the export Data is None")
        return None
    with open(file_path, mode='w') as file:
        for i in data:
            file.write(i+"\n")


if __name__ == '__main__':
    data = get_pdfs_list("merge_pdfs")
    export_file("workspace/outline.txt", data)
