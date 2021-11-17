import os
import xlrd
from pathlib import Path
from pytest_project.config.conf import cm


def get_excel_data_file_name(name):
    """获取xlsx目录"""
    file_name = cm.XLSX_DIR / Path(name)
    if os.path.isfile(file_name):
        return file_name
    else:
        raise FileNotFoundError('没有找到该文件==》{}'.format(file_name))


def getExcelAllData(name, file_name):
    """
    根获取所有数据
    :param name:sheet名
    :param file_name:excel文件在excel_data目录下路径
    :return:
    """
    data = []
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    # 读取sheet
    sheet = book.sheet_by_name(name)
    for row in range(1, sheet.nrows):
        data.append(tuple(sheet.row_values(row, 0, sheet.ncols)))
    return data


def getExcelByRow(name, row_first, row_num, file_name):
    """
    根据行获取所有数据
    :param name: sheet名
    :param row_first: 多少行开始
    :param row_num: 需要多少行
    :param file_name:    文件地址
    :return:
    """
    data = []
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    # 读取sheet
    sheet = book.sheet_by_name(name)
    for row in range(row_first, row_num + row_first):
        try:
            data.append(tuple(sheet.row_values(row, 0, sheet.ncols)))
        except IndexError:
            raise IndexError('请检查xlrd文件==》{}下第{}行没有数据'.format(get_excel_data_file_name(file_name), row + row_first - 1))
    return data


def getExcelOneCol(name, col_index, file_name):
    """
    获取某一列所有数据
    :param name: sheet名
    :param col_index:  列索引
    :param file_name:    文件地址
    :return:
    """
    data = []
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    # 读取sheet
    sheet = book.sheet_by_name(name)
    if col_index <= sheet.ncols:
        for row in range(1, sheet.nrows):
            data.append(sheet.cell_value(row, col_index - 1))
        return data
    else:
        raise IndexError('请检查xlrd文件==》{}下第{}列没有数据'.format(get_excel_data_file_name(file_name), col_index))


def getSheetNames(file_name):
    """
    获取工作簿上所有工资表名
    :param file_name:
    :return:
    """
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    return book.sheet_names()


def getValueByIndex(x, y, sheet_name, file_name):
    """
    获取工作表中某个坐标的值
    :param file_name: 文件名
    :param sheet_name:工作表名
    :param x: 行
    :param y: 列
    :return:
    """
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    sheet = book.sheet_by_name(sheet_name)
    return sheet.cell_value(y-1, x-1)


if __name__ == '__main__':
    # print(getExcelAllData(name='邮箱错误'))
    # print(getExcelByRow('优惠码错误', 1, 3))
    # print(getExcelOneCol('搜索文章', 1, 'Support/support.xlsx'))
    # print(getSheetNames('Protocol/protocol.xlsx').remove('refund'))
    print(get_excel_data_file_name('Protocol/protocol.xlsx'))
