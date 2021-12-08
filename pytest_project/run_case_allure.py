import sys
import subprocess

WIN = sys.platform.startswith('win')
HISTORY = True
DOWNLOAD = True


def main():
    """主函数"""
    steps = [
        "pytest  report\\data --clean-alluredir" if WIN else 'pytest  --alluredir report/data '
                                                             '--clean-alluredir',
        "copy utils\\environment.properties report\\data\\environment.properties" if WIN else 'cp utils/environment'
                                                                                              '.properties '
                                                                                              "report/data"
                                                                                              "/environment"
                                                                                              '.properties',
        "allure generate report\\data -c  -o report/allure" if WIN else '',
        "python pytest_history_trend.py" if WIN else "",
        "python clear_download_dir.py" if WIN else ""
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == '__main__':
    main()
