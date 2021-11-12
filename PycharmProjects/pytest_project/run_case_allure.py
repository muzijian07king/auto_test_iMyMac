import sys
import subprocess

WIN = sys.platform.startswith('win')
HISTORY = True
DOWNLOAD = True


def main():
    """主函数"""
    steps = [
        "venv\\Script\\activate" if WIN else "source venv/bin/activate",
        "pytest  TestCase/discount_test_case/test_discount.py --alluredir allure-results --clean-alluredir",
        "copy utils\\environment.properties allure-results\\environment.properties" if WIN else 'cp utils\environment'
                                                                                                '.properties '
                                                                                                "allure-results"
                                                                                                "/environment"
                                                                                                '.properties',
        "allure generate  allure-results -c  -o report\\allure" if False else "allure generate"
                                                                            "allure-results -c  -o report/allure",
        "python pytest_history_trend.py" if HISTORY else "",
        "python clear_download_dir.py" if DOWNLOAD else "",
        "allure open report/allure " if False else ""
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == '__main__':
    main()
