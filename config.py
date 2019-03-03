# -*- coding:utf8 -*-
import os
import json

MY_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


class ReadConfigJson(object):

    @staticmethod
    def __read_db_json():
        db_config = os.path.join(MY_ROOT_DIR, 'config.json')

        with open(db_config, encoding='utf-8') as f:
            data = f.read()
            data = json.loads(data)
        return data

    def get_mysql_config(self):
        mysql_dict = self.__read_db_json()['mysql']
        mysql_url = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
            user=mysql_dict['user'],
            password=mysql_dict['password'],
            host=mysql_dict['host'],
            port=mysql_dict['port'],
            database=mysql_dict['database'])

        return mysql_url

    @staticmethod
    def get_sqlite_config():
        return 'sqlite:///{}'.format(os.path.join(MY_ROOT_DIR, 'db', 'data.db'))


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = ReadConfigJson().get_mysql_config()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    STATIC_FOLDER = os.path.join(MY_ROOT_DIR, 'static')