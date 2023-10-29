
import PyPDF4
import os

# pip3 install PyPDF4


def create_pdf_handler():
    handler = PdfHandler()
    return handler


class PdfHandler:

    def __init__(self) -> None:
        pass

    def merge_pdfs(self, merge_list_path, result_pdf='result.pdf') -> bool:
        try:
            if os.path.exists(result_pdf):
                print(result_pdf, 'is exist')
                print('merge_pdfs fail')
                return False

            pdf_merger = PyPDF4.PdfFileMerger()

            for path in merge_list_path:
                pdf_merger.append(path)

            with open(result_pdf, "wb") as output_file:
                pdf_merger.write(output_file)

            print('merge_pdfs successfully')
            return True

        except Exception as e:
            print(f"An error occurred: {e}")

    def rotate_pdf(self, in_path, out_path, degree=90):
        try:
            with open(in_path, "rb") as file:
                reader = PyPDF4.PdfFileReader(file)
                writer = PyPDF4.PdfFileWriter()

                for page in reader.pages:
                    # page.rotateClockwise(degree)
                    page.rotateCounterClockwise(degree)
                    writer.addPage(page)

                with open(out_path, "wb") as output_file:
                    writer.write(output_file)
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False


if __name__ == '__main__':
    methods = dir(PdfHandler)
    for m in methods:
        print(m)
