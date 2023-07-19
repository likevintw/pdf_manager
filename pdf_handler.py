import json
import os
import string
from pypdf import PdfMerger


def create_pdf_handler():
    try:
        handler = PdfMerger()
    except:
        pass
        # todo: pip3 install pypdf
        handler = PdfMerger()
    return handler


class pdf_handler:
    def __init__(self) -> None:
        self.handler = None

    def merge_pdfs(self, pdfs, result_name='result.pdf') -> bool:
        try:
            print("read", pdfs)
            for pdf in pdfs:
                print("read {}".format(pdf))
                self.handler.append(pdf)

            self.handler.write(result_name)
            self.handler.close()
            return True

        except:
            print("Merge PDFs Failed")
            return False
