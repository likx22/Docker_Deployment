from app.settings import *

DEBUG = False

# TODO: 修改数据库连接的密码和 IP 地址
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thss',
        'USER': 'root',
        'PASSWORD': '2022012110',
        'HOST': 'mysql',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        },
    }
}
