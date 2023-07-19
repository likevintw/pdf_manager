import json
import os
import string
from pypdf import PdfMerger




class PdfHandler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def merge_pdfs(pdfs, result_name='result.pdf') -> bool:
        try:
            handler=PdfMerger()
            for pdf in pdfs:
                print("read {}".format(pdf))
                handler.append(pdf)
            handler.write(result_name)
            handler.close()
            print("merge pdfs successfully")
            
        except Exception as e:
            print(f"An error occurred: {e}")
