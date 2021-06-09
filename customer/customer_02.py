# !/usr/bin/python3
# encoding: utf-8
import math
import web
import requests
import json


# 本案例将演示从客户系统获取大资源类型的数据,不涉及模拟登陆

class Customer(object):
    def_dicts = {
        'target_ai_url': 'http://192.168.2.202:8088/customer/aiEpResoure/list?pageSize=5000&pageNum=1',
        'target_big_url': 'http://192.168.2.202:8088/customer/bigEpResoure/list?pageSize=5000&pageNum=1',
        'target_ex_url': 'http://192.168.2.202:8088/customer/seaExtension/list?pageSize=10000&pageNum=1',
        'cookie': 'SESSION=MTcwMmUxNDItODgxNi00Mzc1LWFjNjMtNTY5MzNlZTBiYTU1',
        'page_size': 5000,
    }

    def fix_target_url(self, page_num, url_type):
        if url_type == 1:
            resource_url = self.def_dicts.get('target_ai_url')
            target_url = resource_url.replace('pageNum=1', 'pageNum=' + str(page_num), 1)
            return target_url
        if url_type == 2:
            resource_url = self.def_dicts.get('target_big_url')
            target_url = resource_url.replace('pageNum=1', 'pageNum=' + str(page_num), 1)
            return target_url
        if url_type == 3:
            resource_url = self.def_dicts.get('target_ex_url')
            target_url = resource_url.replace('pageNum=1', 'pageNum=' + str(page_num), 1)
            return target_url

    def execute_date(self, rows, url_type):
        # 获取数据库连接
        db_connect = web.database(
            dbn='mysql',
            user='root',
            pw='',
            db='customer_crawler_202103',
            host='127.0.0.1',
            port=3306,
            charset='utf8mb4',
        )
        if url_type == 1:

            # 去重
            for row in rows:
                ai_id = row['aiId']
                if ai_id <= 344191:
                    continue
                db_connect.insert('c_ai_emp',
                                  ai_id=row['aiId'],
                                  ai_r_uuid=row['aiRUuid'],
                                  ai_uuid=row['aiUuid'],
                                  ai_name=row['aiName'],
                                  ai_zone=row['aiZone'],
                                  ai_mobile=row['aiMobile'],
                                  ai_wechat=row['aiWechat'],
                                  ai_groud=row['aiGroud'],
                                  ai_batch=row['aiBatch'],
                                  ai_director=row['aiDistriute'],
                                  ai_res_type=row['aiResType'],
                                  ai_inte_aipro=row['aiInteAipro'],
                                  ai_label=row['aiLabel'],
                                  ai_createtime=row['aiCreatetime'],
                                  ai_my_customer=row['aiMyCustomer'],
                                  ai_isdelete=row['aiIsdelete'],
                                  ai_distriute=row['aiDistriute'],
                                  ai_stage=row['aiStage'],
                                  ai_plan=row['aiPlan'],
                                  ai_group=row['aiGroup'],
                                  ai_dis_person=row['aiDisPerson'],
                                  ai_recent=row['aiRecent'],
                                  ai_recent_time=row['aiRecentTime'],
                                  ai_g_time=row['aiDeptid'],
                                  ai_deptid=row['aiDeptid'],
                                  ai_img=row['aiImg'],
                                  )
        if url_type == 3:
            for row in rows:
                db_connect.insert('c_ex_emp',
                                  c_ex_id=row['cExId'],
                                  c_ex_init=row['cExInit'],
                                  c_ex_source=row['cExSource'],
                                  c_ex_zone=row['cExzone'],
                                  c_ex_chanel=row['cExChanel'],
                                  c_ex_status=row['cExStatus'],
                                  c_ex_zisource=row['cExZiSource'],
                                  c_ex_key=row['cExKey'],
                                  c_ex_name=row['cExName'],
                                  c_ex_phone=row['cExPhone'],
                                  c_ex_mobile=row['cExMobile'],
                                  c_ex_qq=row['cExQq'],
                                  c_ex_wechat=row['cExWechat'],
                                  c_ex_email=row['cExEmail'],
                                  c_ex_intern=row['cExIntern'],
                                  c_ex_groud=row['cExGroud'],
                                  c_ex_remarks=row['cExRemarks'],
                                  c_ex_time=row['cExTime'],
                                  c_ex_creator=row['cExCreator'],
                                  c_ex_flag=row['cExFlag'],
                                  )

    def def_fetch_all(self, url_type):
        # 起始页
        current_page = 1
        # 添加请求头
        headers = {
            'cookie': self.def_dicts.get('cookie')
        }
        reps = requests.get(self.fix_target_url(page_num=current_page, url_type=url_type), headers=headers)
        reps_json = json.loads(reps.text)
        # 计算总页数
        total_row = reps_json['total']
        page_size = self.def_dicts.get('page_size')
        total_page = math.ceil(total_row / page_size)
        print('总页数：%d...' % total_page)
        while current_page <= total_page:
            url = self.fix_target_url(page_num=current_page, url_type=url_type)
            print('开始插入游标 current_page：%d url:%s ...' % (current_page, url))
            reps = requests.get(url, headers=headers)
            reps_json = json.loads(reps.text)
            rows = reps_json['rows']
            self.execute_date(rows=rows, url_type=url_type)
            current_page = current_page + 1
        print('end......')


if __name__ == '__main__':
    cus = Customer()
    cus.def_fetch_all(url_type=1)
