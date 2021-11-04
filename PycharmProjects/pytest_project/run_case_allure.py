import sys
import subprocess

WIN = sys.platform.startswith('win')
HISTORY = True


def main():
    """主函数"""
    steps = [
        "venv\\Script\\activate" if WIN else "source venv/bin/activate",
        "pytest TestCase/sitemap_test_case/test_sitemap.py  --alluredir allure-results --clean-alluredir",
        "copy environment.properties allure-results\\environment.properties" if WIN else 'cp environment.properties '
                                                                                         "allure-results/environment"
                                                                                         '.properties',
        "allure generate  allure-results -c  -o report/allure",
        "python pytest_history_trend.py" if HISTORY else "",
        "allure open report/allure " if WIN else ""
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == '__main__':
    main()
