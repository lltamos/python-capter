# !/usr/bin/python3
# encoding: utf-8
import math
import web
import pymysql
import requests
import json
import pytesseract


# 本案例将演示从客户系统获取大资源类型的数据,不涉及模拟登陆

class Customer(object):
    def_dicts = {
        'target_url': 'http://192.168.2.202:8088/customer/bigEpResoure/list?pageSize=10000&pageNum=1&bpBatch=&bpDirector=&bpColleges=&bpAcademy=&bpMajor=&bpGroud=&bpEpNum=&bpResType=&bpInteProject=&bpSourChanel=&starttime=&endtime=&isBig=&bpEducation=&bpDistribute=&_=1603517383124',
        'cookie': 'SESSION=NDdmNGNkODUtMTVmYi00OTg0LTgxZjctNTg2ZGIwOWU4NDM0;',
        'page_size': 10000,
    }

    def fix_target_url(self, page_num):
        resource_url = self.def_dicts.get('target_url')
        target_url = resource_url.replace('pageNum=1', 'pageNum=' + str(page_num), 1)
        return target_url

    def def_fetch_all(self):
        # 起始页
        current_page = 1
        start_page = 1
        # 添加请求头
        headers = {
            'cookie': self.def_dicts.get('cookie')
        }
        reps = requests.get(self.fix_target_url(start_page), headers=headers)
        reps_json = json.loads(reps.text)
        # 计算总页数
        total_row = reps_json['total']
        page_size = self.def_dicts.get('page_size')
        total_page = math.ceil(total_row / page_size)
        print('BigEmgResource总页数：%d...' % total_page)

        # 获取数据库连接
        db_connect = web.database(
            dbn='mysql',
            user='root',
            pw='',
            db='customer_ crawler',
            host='127.0.0.1',
            port=3306,
        )

        while current_page <= total_page:
            print('开始插入游标 current_page：%d start_page: %d...' % (current_page, start_page))
            reps = requests.get(self.fix_target_url(start_page), headers=headers)
            reps_json = json.loads(reps.text)
            rows = reps_json['rows']
            for row in rows:
                db_connect.insert('c_big_emp',
                                  bp_id=row['bpId'],
                                  bp_r_uuid=row['bpRUuid'],
                                  bp_uuid=row['bpUuid'],
                                  bp_res_type=row['bpResType'],
                                  bp_city=row['bpCity'],
                                  bp_zone=row['bpZone'],
                                  bp_colleges=row['bpColleges'],
                                  bp_academy=row['bpAcademy'],
                                  bp_major=row['bpMajor'],
                                  bp_year=row['bpYear'],
                                  bp_name=row['bpName'],
                                  bp_sex=row['bpSex'],
                                  bp_mobile=row['bpMobile'],
                                  bp_email=row['bpEmail'],
                                  bp_qq=row['bpQq'],
                                  bp_groud_batch=row['bpGroudBatch'],
                                  bp_groud=row['bpGroud'],
                                  bp_batch=row['bpBatch'],
                                  bp_director=row['bpDirector'],
                                  bp_inte_aipro=row['bpInteAipro'],
                                  bp_inte_project=row['bpInteProject'],
                                  bp_sour_chanel=row['bpSourChanel'],
                                  bp_label=row['bpLabel'],
                                  bp_createtime=row['bpCreatetime'],
                                  bp_my_customer=row['bpMyCustomer'],
                                  bp_isdelete=row['bpIsdelete'],
                                  bp_ep_num=row['bpEpNum'],
                                  bp_distriute=row['bpDistribute'],
                                  bp_stage=row['bpStage'],
                                  bp_plan=row['bpPlan'],
                                  bp_group=row['bpGroud'],
                                  bp_dis_person=row['bpDisPerson'],
                                  bp_recent=row['bpRecent'],
                                  bp_recent_time=row['bpRecentTime'],
                                  bp_g_time=row['bpGTime'],
                                  bp_education=row['bpEducation'],
                                  bq_img=row['bpImg']
                                  )
            print('循环插入游标 current_page：%d start_page: %d...' % (current_page, start_page))
            current_page = current_page + 1
            start_page = start_page + 1


if __name__ == '__main__':
    cus = Customer()
    cus.def_fetch_all()
