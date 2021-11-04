import sys
import subprocess

WIN = sys.platform.startswith('win')


def main():
    """主函数"""
    steps = [
        "venv\\Script\\activate" if WIN else "source venv/bin/activate",
        "pytest --lf --alluredir allure-results --clean-alluredir",
        "copy environment.properties allure-results\\environment.properties" if WIN else 'cp environment.properties '
                                                                                         "allure-results/environment"
                                                                                         '.properties',
        "allure generate  allure-results -c  -o report/allure",
        "allure open report/allure " if WIN else ""
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == '__main__':
    main()
