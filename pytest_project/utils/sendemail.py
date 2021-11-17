import zmail
from pytest_project.config.conf import cm


def send_report():
    '''发送报告'''

    with open(cm.get_report_file(), encoding='utf-8') as f:
        content_html = f.read()

    try:
        mail = {
            'from': cm.EMAIL_INFO.get('user_email'),
            'subject': '最新的测试报告邮件',
            'content_html': content_html,
            'attachments': [cm.get_report_file(), ]
        }

        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
    except Exception as e:
        print("发送邮件失败=====》{}！".format(e))

    print('发送成功！')


if __name__ == '__main__':
    send_report()

