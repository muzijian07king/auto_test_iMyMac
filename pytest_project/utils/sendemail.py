import os

import zmail
from pytest_project.config.conf import cm
from pytest_project.utils.compress import compress_dir


def send_report():
    '''发送报告'''

    compress_dir(cm.REPORT_DIR, cm.REPORT_COMPRESS_FILE)
    try:
        mail = {
            'from': cm.EMAIL_INFO.get('user_email'),
            'subject': '最新的iMyMac功能测试报告',
            'content_html': '解压report.zip(接口测试报告)后，请使用allure server 命令打开或者用IDE带服务器插件打开解压目录下的index.html查看报告',
            'attachments': [cm.REPORT_COMPRESS_FILE, ]
        }

        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
    except Exception as e:
        print("发送邮件失败=====》{}！".format(e))

    print('发送成功！')
    os.remove(cm.REPORT_COMPRESS_FILE)


if __name__ == '__main__':
    send_report()