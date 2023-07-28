
import PyPDF4

# pip3 install PyPDF4


class PdfHandler:

    def __init__(self) -> None:
        pass

    @staticmethod
    def merge_pdfs(input_paths, output_path='result.pdf') -> bool:
        try:
            pdf_merger = PyPDF4.PdfFileMerger()

            for path in input_paths:
                pdf_merger.append(path)

            with open(output_path, "wb") as output_file:
                pdf_merger.write(output_file)

        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def rotate_pdf(in_path, out_path, degree=90):
        with open(in_path, "rb") as file:
            reader = PyPDF4.PdfFileReader(file)
            writer = PyPDF4.PdfFileWriter()

            for page in reader.pages:
                page.rotateClockwise(degree)
                writer.addPage(page)

            with open(out_path, "wb") as output_file:
                writer.write(output_file)

    @staticmethod
    def old_merge_pdfs(pdfs, result_name='result.pdf') -> bool:
        pass
        # try:
        #     handler=PyPDF4.PdfFileMerger
        #     ()
        #     for pdf in pdfs:
        #         print("read {}".format(pdf))
        #         handler.append(pdf)
        #     handler.write(result_name)
        #     handler.close()
        #     print("merge pdfs successfully")

        # except Exception as e:
        #     print(f"An error occurred: {e}")


if __name__ == '__main__':
    methods = dir(PdfHandler)
    for m in methods:
        print(m)
