import openpyxl


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


class Operation(object):
    def __init__(self):
        sheet_arr = [
            'A',
            'B',
            'C',
            'D',
            'F',
            'G'
        ]

    def open_file(file_path):
        if not file_path is None:
            pyxl = openpyxl.load_workbook(filename=file_path, read_only=False)
            sheet_list = pyxl.get_sheet_names()
            for index in range(len(sheet_list)):
                sheet = pyxl.get_sheet_by_name(sheet_list[index])
            
        return None
