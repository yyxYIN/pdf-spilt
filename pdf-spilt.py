from PyPDF2 import PdfFileReader, PdfFileWriter
import logging

logging.basicConfig(level=logging.DEBUG)


def spilt_pdf(read_file, output_path, out_page_nums):
    '''
    :param read_file: 读入的pdf文件路径。Input Pdf file path
    :param output_path: 导出文件存放的路径。Export file storage path
    :param out_page_nums: 以out_page_nums页为单位。In out_page_nums pages
    :return:
    '''
    try:
        fp_read_file = open(read_file, 'rb')
        pdf_input_file = PdfFileReader(fp_read_file)
        page_count = pdf_input_file.getNumPages()
        logging.info('page count is %d', page_count)

        loop_num = round(page_count / out_page_nums)
        logging.info('loop count is %d', loop_num)
        last_pages_num = page_count - out_page_nums * loop_num
        logging.info('last_pages_num count is %d', last_pages_num)

        for i in range(0, out_page_nums * loop_num, out_page_nums):
            pdf_output_name = output_path + "\\" + str(i + 1) + '-' + str(i + out_page_nums) + '.pdf'
            try:
                pdf_output_file = PdfFileWriter()
                for j in range(i, i + out_page_nums):
                    pdf_output_file.addPage(pdf_input_file.getPage(j))
                with open(pdf_output_name, 'wb') as sub_fp:
                    pdf_output_file.write(sub_fp)
                logging.info('完成分割%d到%d页', i + 1, i + out_page_nums)
            except IndexError as e:
                logging.debug(e)

        if last_pages_num != 0:
            pdf_output_name = output_path + "\\" + str(out_page_nums * loop_num + 1) + '-' + str(out_page_nums * loop_num + last_pages_num) + '.pdf'
            try:
                pdf_output_file = PdfFileWriter()
                for i in range(out_page_nums * loop_num, out_page_nums * loop_num + last_pages_num):
                    pdf_output_file.addPage(pdf_input_file.getPage(i))
                with open(pdf_output_name, 'wb') as sub_fp:
                    pdf_output_file.write(sub_fp)
                logging.info('完成分割%d到%d页', i + 1, i + out_page_nums)
            except IndexError as e:
                logging.debug(e)

    except Exception as e:
        logging.debug(e)
    finally:
        fp_read_file.close()
        logging.info('finish')


if __name__ == "__main__":
    FILE_NAME = "C:\\Users\\42035\Desktop\\linearalgebra\\Introduction to Linear Algebra(5th edition 2016).pdf"
    output_path = "C:\\Users\\42035\Desktop\\linearalgebra"
    spilt_pdf(FILE_NAME, output_path, 80)