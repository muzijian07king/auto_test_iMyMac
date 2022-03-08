import os
import xlrd
from pathlib import Path

from pytest_project.config.conf import cm
from pytest_project.utils.logger import log
import openpyxl
import threading

from pytest_project.utils.times import sleep


def get_excel_data_file_name(name):
    """获取xlsx目录"""
    file_name = cm.XLSX_DIR / Path(name)
    if os.path.isfile(file_name):
        return file_name
    else:
        raise FileNotFoundError('没有找到该文件==》{}'.format(file_name))


def set_excel_data(name, file_name, x, y, value):
    """
    修改excel
    :param name: sheet名
    :param file_name: 文件路径
    :param x: 横坐标
    :param y: 纵坐标
    :param value: 修改的值
    :return:
    """
    try:
        book = openpyxl.load_workbook(get_excel_data_file_name(file_name))
        sheet = book[name]
        sheet.cell(y, x).value = value
        log.info(f'对工作簿{file_name}的工作表{name}的（{y}，{x}）单元格值修改成{value}')
        book.save(get_excel_data_file_name(file_name))
    except IOError:
        log.error('修改xlsx失败')
        raise IOError('文件已被占用')


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
    log.info(f'xlsx提取到：{data}')
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
            raise IndexError(
                '请检查xlrd文件==》{}下工作表{}第{}行没有数据'.format(get_excel_data_file_name(file_name), name, row + row_first - 1))
    log.info(f'xlsx提取到：{data}')
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
        log.info(f'xlsx提取到：{data}')
        return data
    else:
        raise IndexError('请检查xlrd文件==》{}下下工作表{}第{}列没有数据'.format(get_excel_data_file_name(file_name), name, col_index))


def getSheetNames(file_name):
    """
    获取工作簿上所有工资表名
    :param file_name:
    :return:
    """
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    value = book.sheet_names()
    log.info(f'xlsx提取到：{value}')
    return value


def getValueByIndex(x, y, sheet_name, file_name):
    """
    获取工作表中某个坐标的值
    :param file_name: 文件名
    :param sheet_name:工作表名
    :param x: 横坐标  （A~Z）
    :param y: 纵坐标   (1~100)
    :return:
    """
    # 打开xlsx文件
    book = xlrd.open_workbook(get_excel_data_file_name(file_name))
    sheet = book.sheet_by_name(sheet_name)
    value = sheet.cell_value(y - 1, x - 1)
    log.info(f'xlsx提取到：{value}')
    return value


if __name__ == '__main__':
    getExcelByRow('修改成功', 1, 1, 'Admin/user.xlsx')
