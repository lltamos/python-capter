# !/usr/bin/python3
# encoding: utf-8
import web
import os


# 本案例将演示从客户系统获取大资源类型的数据,不涉及模拟登陆

class DbProvider(object):

    def get_data_source(self):
        db = web.database(
            dbn='mysql',
            user='root',
            pw='',
            db='qbs',
            host='127.0.0.1',
            port=3306
        )
        results = db.query('select * from qbs.cur_course_docs order by id asc')
        sum_count = 1
        for result in results:
            # if result['id'] > 3009:
            #     break
            # if 2995 <= result['id'] <= 3009:
            if result['id'] == 3000:
                file_url = result['file_path']
                str_list = file_url.split('/')
                file_name_pre = str_list[-1]
                result_file_name = str(result['id']) + '_' + result['file_name'] + '_' + file_name_pre
                os.system(
                    'cd /Users/Exx/Desktop/fileworks ; wget -c -O ' + '"' + result_file_name + '"' + ' ' + '"' + file_url + '"')
                print('创建并写入文件:{%s}完成' % result_file_name)
                break


if __name__ == '__main__':
    provider = DbProvider()
    provider.get_data_source()
