import allure
import pytest
from pytest_project.common.readexcel import getExcelAllData
from pytest_project.page_object.faq.faqs_page import FAQSPage
from pytest_project.common.readconfig import ini


@allure.feature('FAQ页面测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = FAQSPage(drivers)
        self.driver.get_url(ini.get_url('faq'))

    @allure.title('测试跳转register帮助页面')
    @allure.tag('register常见问题')
    @allure.story('跳转常见问题测试')
    def test_001(self):
        self.driver.goto_register()
        self.driver.assert_goto_register()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转activate帮助页面')
    @allure.tag('activate常见问题')
    def test_002(self):
        self.driver.goto_activate()
        self.driver.assert_goto_activate()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转order常见问题页面')
    @allure.tag('order常见问题')
    def test_003(self):
        self.driver.goto_order()
        self.driver.assert_goto_order()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转到refund页面')
    @allure.tag('refund')
    def test_004(self):
        self.driver.goto_refund()
        self.driver.assert_goto_refund()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转PowerMyMac常见问题页面')
    @allure.tag('PowerMyMac常见问题')
    def test_005(self):
        self.driver.goto_PowerMyMac()
        self.driver.assert_goto_PowerMyMac()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转Video常见问题页面')
    @allure.tag('Video常见问题')
    def test_006(self):
        self.driver.goto_Video()
        self.driver.assert_goto_Video()

    @allure.story('跳转常见问题测试')
    @allure.title('测试跳转PDF常见问题页面')
    @allure.tag('PDF常见问题')
    def test_007(self):
        self.driver.goto_PDF()
        self.driver.assert_goto_PDF()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签1跳转')
    @allure.tag('书签1')
    def test_008(self):
        self.driver.goto_register()
        self.driver.click_question_one()
        self.driver.assert_goto_question_one()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签2跳转')
    @allure.tag('书签2')
    def test_009(self):
        self.driver.goto_register()
        self.driver.click_question_two()
        self.driver.assert_goto_question_two()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3跳转')
    @allure.tag('书签3')
    def test_010(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.assert_goto_question_three()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签4跳转')
    @allure.tag('书签4')
    def test_011(self):
        self.driver.goto_register()
        self.driver.click_question_four()
        self.driver.assert_goto_question_four()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题1跳转')
    @allure.tag('问题1')
    def test_012(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_1()
        self.driver.assert_goto_step_1()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题2跳转')
    @allure.tag('问题2')
    def test_013(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_2()
        self.driver.assert_goto_step_2()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题3跳转')
    @allure.tag('问题3')
    def test_014(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_3()
        self.driver.assert_goto_step_3()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题4跳转')
    @allure.tag('问题4')
    def test_015(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_4()
        self.driver.assert_goto_step_4()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题5跳转')
    @allure.tag('问题5')
    def test_016(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_5()
        self.driver.assert_goto_step_5()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题6跳转')
    @allure.tag('问题6')
    def test_017(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_6()
        self.driver.assert_goto_step_6()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题7跳转')
    @allure.tag('问题7')
    def test_018(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_7()
        self.driver.assert_goto_step_7()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题8跳转')
    @allure.tag('问题8')
    def test_019(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_8()
        self.driver.assert_goto_step_8()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题9跳转')
    @allure.tag('问题9')
    def test_020(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_9()
        self.driver.assert_goto_step_9()

    @allure.story('register常见问题测试')
    @allure.title('测试侧边栏书签3的问题10跳转')
    @allure.tag('问题10')
    def test_021(self):
        self.driver.goto_register()
        self.driver.click_question_three()
        self.driver.click_question_three_step_10()
        self.driver.assert_goto_step_10()

    @allure.story('activate常见问题测试')
    @allure.title('测试开启书签')
    @allure.tag('开启书签')
    def test_022(self):
        self.driver.goto_activate()
        self.driver.click_content_hide()
        self.driver.assert_show_content()

    @allure.story('activate常见问题测试')
    @allure.title('测试隐藏书签')
    @allure.tag('隐藏书签')
    def test_023(self):
        self.driver.goto_activate()
        self.driver.click_content_show()
        self.driver.assert_hide_content()

    @allure.story('activate常见问题测试')
    @allure.title('测试书签1跳转')
    @allure.tag('书签1')
    def test_024(self):
        self.driver.goto_activate()
        self.driver.assert_part1()

    @allure.story('activate常见问题测试')
    @allure.title('测试书签2跳转')
    @allure.tag('书签2')
    def test_025(self):
        self.driver.goto_activate()
        self.driver.assert_part2()

    @allure.story('activate常见问题测试')
    @allure.title('测试书签3跳转')
    @allure.tag('书签3')
    def test_026(self):
        self.driver.goto_activate()
        self.driver.assert_part3()

    @allure.story('activate常见问题测试')
    @allure.title('测试导航栏上的logo跳转')
    @allure.tag('logo')
    def test_027(self):
        self.driver.goto_activate()
        self.driver.goto_context()
        self.driver.click_logo()
        self.driver.assert_goto_logo_index()

    @allure.story('activate常见问题测试')
    @allure.title('测试导航栏上的下载')
    @allure.tag('下载')
    def test_028(self):
        self.driver.goto_activate()
        self.driver.goto_context()
        self.driver.click_nav_download()
        self.driver.assert_download()

    @allure.story('activate常见问题测试')
    @allure.title('测试导航栏上的购买')
    @allure.tag('购买')
    def test_029(self):
        self.driver.goto_activate()
        self.driver.goto_context()
        self.driver.click_nav_buy()
        self.driver.assert_goto_buy()

    @allure.story('activate常见问题测试')
    @allure.title('测试侧边弹窗上的下载')
    @allure.tag('下载')
    def test_030(self):
        self.driver.goto_activate()
        self.driver.goto_context()
        self.driver.click_sidebar_download()
        self.driver.assert_download()

    @allure.story('activate常见问题测试')
    @allure.title('测试关闭侧边弹窗')
    @allure.tag('侧边弹窗')
    def test_031(self):
        self.driver.goto_activate()
        self.driver.goto_context()
        self.driver.click_sidebar_close()
        self.driver.assert_close_sidebar()

    @allure.story('activate常见问题测试')
    @allure.title('测试鼠标悬停在一颗星评价功能')
    @allure.tag('poor')
    def test_032(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.scroll_grade_poor()
        self.driver.assert_grade(1)

    @allure.story('activate常见问题测试')
    @allure.title('测试鼠标悬停在两颗星评价功能')
    @allure.tag('fair')
    def test_033(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.scroll_grade_fair()
        self.driver.assert_grade(2)

    @allure.story('activate常见问题测试')
    @allure.title('测试鼠标悬停在三颗星评价功能')
    @allure.tag('average')
    def test_034(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.scroll_grade_average()
        self.driver.assert_grade(3)

    @allure.story('activate常见问题测试')
    @allure.title('测试鼠标悬停在四颗星评价功能')
    @allure.tag('good')
    def test_035(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.scroll_grade_good()
        self.driver.assert_grade(4)

    @allure.story('activate常见问题测试')
    @allure.title('测试鼠标悬停在五颗星评价功能')
    @allure.tag('excellent')
    def test_036(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.scroll_grade_excellent()
        self.driver.assert_grade(5)

    @allure.story('activate常见问题测试')
    @allure.title('测试提交一颗星评价功能')
    @allure.tag('poor')
    def test_037(self):
        self.driver.goto_activate()
        self.driver.delete_grade_cookie()
        self.driver.scroll_star()
        num = self.driver.get_grade_num()
        self.driver.click_grade_poor()
        self.driver.assert_submit_grade(1, num)

    @allure.story('activate常见问题测试')
    @allure.title('测试提交两颗星评价功能')
    @allure.tag('fair')
    def test_038(self):
        self.driver.goto_activate()
        self.driver.delete_grade_cookie()
        self.driver.scroll_star()
        num = self.driver.get_grade_num()
        self.driver.click_grade_fair()
        self.driver.assert_submit_grade(2, num)

    @allure.story('activate常见问题测试')
    @allure.title('测试提交三颗星评价功能')
    @allure.tag('average')
    def test_039(self):
        self.driver.goto_activate()
        self.driver.delete_grade_cookie()
        self.driver.scroll_star()
        num = self.driver.get_grade_num()
        self.driver.click_grade_average()
        self.driver.assert_submit_grade(3, num)

    @allure.story('activate常见问题测试')
    @allure.title('测试提交四颗星评价功能')
    @allure.tag('good')
    def test_040(self):
        self.driver.goto_activate()
        self.driver.delete_grade_cookie()
        self.driver.scroll_star()
        num = self.driver.get_grade_num()
        self.driver.click_grade_good()
        self.driver.assert_submit_grade(4, num)

    @allure.story('activate常见问题测试')
    @allure.title('测试提交五颗星评价功能')
    @allure.tag('excellent')
    def test_041(self):
        self.driver.goto_activate()
        self.driver.delete_grade_cookie()
        self.driver.scroll_star()
        num = self.driver.get_grade_num()
        self.driver.click_grade_excellent()
        self.driver.assert_submit_grade(5, num)

    @allure.story('activate常见问题测试')
    @allure.title('测试跳转到评论栏功能')
    @allure.tag('评论栏')
    def test_042(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.assert_goto_comment()

    @allure.story('activate常见问题测试')
    @allure.title('测试跳转到编辑评论功能')
    @allure.tag('编辑评论')
    def test_043(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.assert_goto_leave_comment()

    @allure.story('activate常见问题测试')
    @allure.title('测试错误格式提交评论功能')
    @allure.tag('提交失败评论')
    @pytest.mark.parametrize('name,email,context,name_class,email_class,context_class',
                             getExcelAllData('错误格式评论', 'FAQ\\faq.xlsx'))
    def test_044(self, name, email, context, name_class, email_class, context_class):
        self.driver.goto_activate()
        self.driver.scroll_input()
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_context(context)
        self.driver.submit_comment()
        self.driver.assert_input_error(name_class, email_class, context_class)

    @allure.story('activate常见问题测试')
    @allure.title('测试成功格式提交评论功能')
    @allure.tag('成功提交评论')
    @pytest.mark.parametrize('name,email,context', getExcelAllData('正确格式评论', 'FAQ\\faq.xlsx'))
    def test_045(self, name, email, context):
        self.driver.goto_activate()
        self.driver.scroll_input()
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_context(context)
        self.driver.submit_comment()
        self.driver.assert_input_succeed_data(name, context)

    @allure.story('activate常见问题测试')
    @allure.title('测试底部下载按钮')
    @allure.tag('下载')
    def test_046(self):
        self.driver.goto_activate()
        self.driver.scroll_star()
        self.driver.click_sidebar_bottom()
        self.driver.assert_download()

    @allure.story('activate常见问题测试')
    @allure.title('测试底部文章跳转')
    @allure.tag('第一篇文章')
    def test_047(self):
        self.driver.goto_activate()
        self.driver.scroll_article()
        self.driver.click_bottom_article_one()
        self.driver.assert_goto_article_one()

    @allure.story('activate常见问题测试')
    @allure.title('测试底部文章跳转')
    @allure.tag('第二篇文章')
    def test_048(self):
        self.driver.goto_activate()
        self.driver.scroll_article()
        self.driver.click_bottom_article_two()
        self.driver.assert_goto_article_two()

    @allure.story('activate常见问题测试')
    @allure.title('测试底部文章跳转')
    @allure.tag('第三篇文章')
    def test_049(self):
        self.driver.goto_activate()
        self.driver.scroll_article()
        self.driver.click_bottom_article_three()
        self.driver.assert_goto_article_three()

    @allure.story('activate常见问题测试')
    @allure.title('测试底部文章跳转')
    @allure.tag('第四篇文章')
    def test_050(self):
        self.driver.goto_activate()
        self.driver.scroll_article()
        self.driver.click_bottom_article_four()
        self.driver.assert_goto_article_four()

    @allure.story('order常见问题测试')
    @allure.title('测试order常见问题的展开功能')
    @allure.tag('展开问题')
    def test_051(self):
        self.driver.goto_order()
        self.driver.unfold_faqs()
        self.driver.assert_faqs_unfold()

    @allure.story('order常见问题测试')
    @allure.title('测试order常见问题的折叠功能')
    @allure.tag('折叠问题')
    def test_052(self):
        self.driver.goto_order()
        self.driver.fold_faqs()
        self.driver.assert_faqs_fold()

    @allure.story('PowerMyMac常见问题测试')
    @allure.title('测试PowerMyMac常见问题的展开功能')
    @allure.tag('展开问题')
    def test_053(self):
        self.driver.goto_PowerMyMac()
        self.driver.unfold_faqs()
        self.driver.assert_faqs_unfold()

    @allure.story('PowerMyMac常见问题测试')
    @allure.title('测试PowerMyMac常见问题的折叠功能')
    @allure.tag('折叠问题')
    def test_054(self):
        self.driver.goto_PowerMyMac()
        self.driver.fold_faqs()
        self.driver.assert_faqs_fold()

    @allure.story('Video常见问题测试')
    @allure.title('测试Video常见问题的展开功能')
    @allure.tag('展开问题')
    def test_055(self):
        self.driver.goto_Video()
        self.driver.unfold_faqs()
        self.driver.assert_faqs_unfold()

    @allure.story('Video常见问题测试')
    @allure.title('测试Video常见问题的折叠功能')
    @allure.tag('折叠问题')
    def test_056(self):
        self.driver.goto_Video()
        self.driver.fold_faqs()
        self.driver.assert_faqs_fold()

    @allure.story('PDF常见问题测试')
    @allure.title('测试PDF常见问题的展开功能')
    @allure.tag('展开问题')
    def test_057(self):
        self.driver.goto_PDF()
        self.driver.unfold_faqs()
        self.driver.assert_faqs_unfold()

    @allure.story('PDF常见问题测试')
    @allure.title('测试PDF常见问题的折叠功能')
    @allure.tag('折叠问题')
    def test_058(self):
        self.driver.goto_PDF()
        self.driver.fold_faqs()
        self.driver.assert_faqs_fold()
