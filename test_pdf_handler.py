import unittest
import pdf_handler

# python3 -m unittest test_pdf_handler.py


class TestStringMethods(unittest.TestCase):

    @unittest.skip("passed 20230729")
    def test_merge_pdfs(self):
        handler = pdf_handler.create_pdf_handler()
        merge_list_path = []
        merge_list_path.append(
            '/Users/kevin/Desktop/file_space/文件_2023-06-23_165956_2.pdf')
        merge_list_path.append(
            '/Users/kevin/Desktop/file_space/文件_2023-06-23_165956_3.pdf')
        result_pdf = '/Users/kevin/Desktop/file_space/merge_result.pdf'
        assert handler.merge_pdfs(merge_list_path, result_pdf) == True

    @unittest.skip("passed 20230729")
    def test_rotate_pdf(self):
        handler = pdf_handler.create_pdf_handler()
        input_pdf_path = '/Users/kevin/Desktop/file_space/merge_result.pdf'
        output_pdf_path = '/Users/kevin/Desktop/file_space/rotated_result.pdf'
        assert handler.rotate_pdf(input_pdf_path, output_pdf_path, 90) == True


if __name__ == '__main__':
    unittest.main()
