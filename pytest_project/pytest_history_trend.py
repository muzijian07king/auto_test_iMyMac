import json, os

"""
本地进行记录测试结果，并在allure上显示
"""


def t():
    with open('utils/history-trend.json', 'r') as file:
        before_data = json.load(file)

    with open('report/allure/widgets/history-trend.json', 'r') as file:
        after_data = json.load(file)

    with open('report/allure/widgets/history-trend.json', 'w') as file:
        if len(before_data) < 1:
            after_data[0].setdefault("buildOrder", 1)
        else:
            after_data[0]["buildOrder"] = before_data[0]["buildOrder"] + 1

        before_data.extend(after_data)
        before_data.sort(key=lambda x: x["buildOrder"], reverse=True)
        json.dump(before_data[:15], file)

    with open('utils/history-trend.json', 'w') as file:
        json.dump(before_data[:15], file)


t()
