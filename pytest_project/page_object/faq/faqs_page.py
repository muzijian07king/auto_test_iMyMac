import datetime
from pytest_project.utils.times import sleep
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
import allure
from pytest_project.config.conf import cm
from pytest_project.common.readexcel import getValueByIndex

faqs = Element('FAQ/index')


class FAQSPage(WebPage):

    @allure.step('跳转register帮助页面')
    def goto_register(self):
        self.is_click(faqs.readYaml('$.Register.link'))

    @allure.step('跳转activate帮助页面')
    def goto_activate(self):
        self.is_click(faqs.readYaml('$.Activate.link'))

    @allure.step('跳转order常见问题页面')
    def goto_order(self):
        self.is_click(faqs.readYaml('$.Order.link'))

    @allure.step('跳转Refund页面')
    def goto_refund(self):
        self.is_click(faqs.readYaml('$.Refund.link'))

    @allure.step('跳转PowerMyMac常见问题页面')
    def goto_PowerMyMac(self):
        self.is_click(faqs.readYaml('$.PowerMyMac-FAQs.link'))

    @allure.step('跳转Video常见问题页面')
    def goto_Video(self):
        self.is_click(faqs.readYaml('$.Video-Converter-FAQs.link'))

    @allure.step('跳转PDF常见问题页面')
    def goto_PDF(self):
        self.scroll_to_loc_is_click(faqs.readYaml('$.PDF-Compressor-FAQs.link'))

    def assert_goto_register(self):
        self.allure_assert('判断成功跳转页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/powermymac/user-guide.html'))

    def assert_goto_activate(self):
        self.allure_assert('判断成功跳转页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/mac-tips/account-center.html'))

    def assert_goto_order(self):
        self.allure_assert('判断成功跳转页面', ('eq', self.get_current_url(), 'https://www.imymac.com/faqs/sales-faq/'))

    def assert_goto_refund(self):
        self.allure_assert('判断成功跳转页面', ('eq', self.get_current_url(), 'https://www.imymac.com/refund.html'))

    def assert_goto_PowerMyMac(self):
        self.allure_assert('判断成功跳转页面', ('eq', self.get_current_url(), 'https://www.imymac.com/faqs/powermymac/'))

    def assert_goto_Video(self):
        self.allure_assert('判断成功跳转页面', ('eq', self.get_current_url(), 'https://www.imymac.com/faqs/video-converter/'))

    def assert_goto_PDF(self):
        self.allure_assert('判断成功跳转页面', ('eq', self.get_current_url(), 'https://www.imymac.com/faqs/pdf-compressor/'))

    @allure.step('点击侧边栏问题1移动到指定位置')
    def click_question_one(self):
        self.scroll_to_loc_is_click(faqs.readYaml("$.Register.item-a.one"))
        sleep(2)

    @allure.step('点击侧边栏问题2移动到指定位置')
    def click_question_two(self):
        self.scroll_to_loc_is_click(faqs.readYaml("$.Register.item-a.two"))
        sleep(2)

    @allure.step('点击侧边栏问题3移动到指定位置')
    def click_question_three(self):
        self.scroll_to_loc_is_click(faqs.readYaml("$.Register.item-a.three"))
        sleep(2)

    @allure.step('点击侧边栏问题4移动到指定位置')
    def click_question_four(self):
        self.scroll_to_loc_is_click(faqs.readYaml("$.Register.item-a.four"))
        sleep(2)

    def assert_goto_question_one(self):
        self.allure_assert('判断成功移动到指定位置',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 373px;'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'class'), 'guide-nav is_fix'))

    def assert_goto_question_two(self):
        self.allure_assert('判断成功移动到指定位置',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 2341px;'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'class'), 'guide-nav is_fix'))

    def assert_goto_question_three(self):
        self.allure_assert('判断成功移动到指定位置',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 4379px;'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'class'), 'guide-nav is_fix'))

    def assert_goto_question_four(self):
        self.allure_assert('判断成功移动到指定位置',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 24701px;'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'class'), 'guide-nav is_fix'))

    @allure.step("点击问题3中第一个方法")
    def click_question_three_step_1(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.one'), 1)

    @allure.step("点击问题3中第二个方法")
    def click_question_three_step_2(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.two'), 1)

    @allure.step("点击问题3中第三个方法")
    def click_question_three_step_3(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.three'), 1)

    @allure.step("点击问题3中第四个方法")
    def click_question_three_step_4(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.four'), 1)

    @allure.step("点击问题3中第五个方法")
    def click_question_three_step_5(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.five'), 1)

    @allure.step("点击问题3中第六个方法")
    def click_question_three_step_6(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.six'), 1)

    @allure.step("点击问题3中第七个方法")
    def click_question_three_step_7(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.seven'), 1)

    @allure.step("点击问题3中第八个方法")
    def click_question_three_step_8(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.eight'), 1)

    @allure.step("点击问题3中第九个方法")
    def click_question_three_step_9(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.nine'), 1)

    @allure.step("点击问题3中第十个方法")
    def click_question_three_step_10(self):
        self.is_click(faqs.readYaml('$.Register.nav-list.ten'), 1)

    def assert_goto_step_1(self):
        self.allure_assert('判断成功跳转到第一个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.one'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 4699px;'))

    def assert_goto_step_2(self):
        self.allure_assert('判断成功跳转到第二个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.two'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 5533px;'))

    def assert_goto_step_3(self):
        self.allure_assert('判断成功跳转到第三个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.three'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 7968px;'))

    def assert_goto_step_4(self):
        self.allure_assert('判断成功跳转到第四个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.four'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 10248px;'))

    def assert_goto_step_5(self):
        self.allure_assert('判断成功跳转到第五个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.five'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 14888px;'))

    def assert_goto_step_6(self):
        self.allure_assert('判断成功跳转到第六个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.six'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 17585px;'))

    def assert_goto_step_7(self):
        self.allure_assert('判断成功跳转到第七个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.seven'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 19721px;'))

    def assert_goto_step_8(self):
        self.allure_assert('判断成功跳转到第八个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.eight'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 12608px;'))

    def assert_goto_step_9(self):
        self.allure_assert('判断成功跳转到第九个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.nine'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 21383px;'))

    def assert_goto_step_10(self):
        self.allure_assert('判断成功跳转到第十个方法',
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav-list.ten'), 'class'), 'active'),
                           ('eq', self.getAttribute(faqs.readYaml('$.Register.nav'), 'style'), 'top: 23605px;'))

    @allure.step('点击开启书签按钮')
    def click_content_hide(self):
        self.jsInDriver(f"document.querySelector({faqs.readYaml('$.Activate.contents.hide')}).click()")
        self.jsInDriver(f"document.querySelector({faqs.readYaml('$.Activate.contents.hide')}).click()")

    @allure.step('点击关闭书签按钮')
    def click_content_show(self):
        self.jsInDriver(f"document.querySelector({faqs.readYaml('$.Activate.contents.hide')}).click()")

    def assert_show_content(self):
        self.allure_assert('判断开启书签', (
            'eq', self.getAttribute(faqs.readYaml('$.Activate.contents.hide'), 'guidetitle-after-value'), 'Hide'))

    def assert_hide_content(self):
        self.allure_assert('判断隐藏书签', (
            'eq', self.getAttribute(faqs.readYaml('$.Activate.contents.hide'), 'guidetitle-after-value'), 'Show'))

    def assert_part1(self):
        self.allure_assert('判断书签1是否跳转', ('eq', self.getAttribute(faqs.readYaml('$.Activate.contents.part1'), 'href'),
                                         'https://www.imymac.com/mac-tips/account-center.html#part1'),
                           ('not_eq', self.find_element(('css', '#part1')), None))

    def assert_part2(self):
        self.allure_assert('判断书签2是否跳转', ('eq', self.getAttribute(faqs.readYaml('$.Activate.contents.part2'), 'href'),
                                         'https://www.imymac.com/mac-tips/account-center.html#part2'),
                           ('not_eq', self.find_element(('css', '#part2')), None))

    def assert_part3(self):
        self.allure_assert('判断书签3是否跳转', ('eq', self.getAttribute(faqs.readYaml('$.Activate.contents.part3'), 'href'),
                                         'https://www.imymac.com/mac-tips/account-center.html#part3'),
                           ('not_eq', self.find_element(('css', '#part3')), None))

    @allure.step('移动到正文首行')
    def goto_context(self):
        self.is_click(faqs.readYaml('$.Activate.contents.part1'), 1)

    @allure.step('点击logo')
    def click_logo(self):
        self.is_click(faqs.readYaml('$.Activate.nav.logo'))

    @allure.step('点击导航栏上的下载按钮')
    def click_nav_download(self):
        self.is_click(faqs.readYaml('$.Activate.nav.download'))

    @allure.step('点击导航栏上的购买按钮')
    def click_nav_buy(self):
        self.is_click(faqs.readYaml('$.Activate.nav.buy'))

    def assert_goto_logo_index(self):
        self.allure_assert('判断logo按钮跳转官网', ('eq', self.get_current_url(), 'https://www.imymac.com/powermymac/'))

    def assert_download(self):
        self.allure_assert_or('判断下载是否成功', ('eq', cm.get_download_filename(), 'crdownload'),
                              ('eq', cm.get_download_filename(), 'pkg'))

    def assert_goto_buy(self):
        self.allure_assert('判断跳转购买pmm',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/store/buy-powermymac.html'))

    @allure.step('点击侧边弹窗的下载按钮')
    def click_sidebar_download(self):
        self.is_click(faqs.readYaml('$.Activate.sidebar.download'))

    @allure.step('关闭侧边弹窗')
    def click_sidebar_close(self):
        self.is_click(faqs.readYaml('$.Activate.sidebar.close'))

    def assert_close_sidebar(self):
        self.allure_assert('判断关闭侧边弹窗', ('eq', self.getAttribute(faqs.readYaml('$.Activate.sidebar.sidebar'),
                                                                'class'), 'sidebar text-center pm-bg sidebar-normal'))

    @allure.step('滑动到评论栏')
    def scroll_star(self):
        self.scroll_to_loc(faqs.readYaml('$.Activate.grade.index'))
        self.scroll_by_x_y(0, -200)

    @allure.step('鼠标悬停在一颗星评价')
    def scroll_grade_poor(self):
        self.move_element(faqs.readYaml('$.Activate.grade.poor'))

    @allure.step('鼠标悬停在二颗星评价')
    def scroll_grade_fair(self):
        self.move_element(faqs.readYaml('$.Activate.grade.fair'))

    @allure.step('鼠标悬停在三颗星评价')
    def scroll_grade_average(self):
        self.move_element(faqs.readYaml('$.Activate.grade.average'))

    @allure.step('鼠标悬停在四颗星评价')
    def scroll_grade_good(self):
        self.move_element(faqs.readYaml('$.Activate.grade.good'))

    @allure.step('鼠标悬停在五颗星评价')
    def scroll_grade_excellent(self):
        self.move_element(faqs.readYaml('$.Activate.grade.excellent'))

    def assert_grade(self, star):
        star = star + 1
        self.allure_assert(f'判断评价{star - 1}星是否可选中', (
            'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.poor'), 'class'),
            getValueByIndex(2, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.fair'), 'class'),
                               getValueByIndex(3, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.average'), 'class'),
                               getValueByIndex(4, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.good'), 'class'),
                               getValueByIndex(5, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.excellent'), 'class'),
                               getValueByIndex(6, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.element_text(faqs.readYaml('$.Activate.grade.grade')),
                               getValueByIndex(1, star, '评价', 'FAQ/faq.xlsx')))

    @allure.step('获取当前评论数')
    def get_grade_num(self):
        return self.element_text(faqs.readYaml('$.Activate.grade.grade-num'))

    @allure.step('提交poor评价')
    def click_grade_poor(self):
        self.is_click(faqs.readYaml('$.Activate.grade.poor'))

    @allure.step('提交fair评价')
    def click_grade_fair(self):
        self.is_click(faqs.readYaml('$.Activate.grade.fair'))

    @allure.step('提交average评价')
    def click_grade_average(self):
        self.is_click(faqs.readYaml('$.Activate.grade.average'))

    @allure.step('提交good评价')
    def click_grade_good(self):
        self.is_click(faqs.readYaml('$.Activate.grade.good'))

    @allure.step('提交excellent评价')
    def click_grade_excellent(self):
        self.is_click(faqs.readYaml('$.Activate.grade.excellent'))

    def delete_grade_cookie(self):
        self.delete_all_cookie()
        self.refresh()

    def assert_submit_grade(self, star, num):
        star = star + 1
        self.allure_assert(f'判断评价{star - 1}星是否可选中', (
            'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.poor'), 'class'),
            getValueByIndex(2, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.fair'), 'class'),
                               getValueByIndex(3, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.average'), 'class'),
                               getValueByIndex(4, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.good'), 'class'),
                               getValueByIndex(5, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.getAttribute(faqs.readYaml('$.Activate.grade.excellent'), 'class'),
                               getValueByIndex(6, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.element_text(faqs.readYaml('$.Activate.grade.grade')),
                               getValueByIndex(1, star, '评价', 'FAQ/faq.xlsx')), (
                               'eq', self.element_text(faqs.readYaml('$.Activate.grade.grade-num')), str(int(num) + 1)))

    def assert_goto_comment(self):
        href = self.getAttribute(faqs.readYaml('$.Activate.comment.comment'), 'href')
        self.allure_assert('判断跳转到评论栏',
                           ('not_eq', self.find_element(('css', f"#{href.split('#')[1]}")), None))

    def assert_goto_leave_comment(self):
        href = self.getAttribute(faqs.readYaml('$.Activate.comment.leave-comment'), 'href')
        self.allure_assert('判断跳转到发布评论栏',
                           ('not_eq', self.find_element(('css', f"#{href.split('#')[1]}")), None))

    @allure.step('滑动到评论栏')
    def scroll_input(self):
        self.scroll_to_loc(faqs.readYaml('$.Activate.comment.input.index'))

    @allure.step('输入用户名')
    def input_name(self, name):
        self.input_text(faqs.readYaml('$.Activate.comment.input.name'), name)

    @allure.step('输入邮箱')
    def input_email(self, email):
        self.input_text(faqs.readYaml('$.Activate.comment.input.email'), email)

    @allure.step('输入内容')
    def input_context(self, context):
        self.input_text(faqs.readYaml('$.Activate.comment.input.context'), context)

    @allure.step('点击提交评论按钮')
    def submit_comment(self):
        self.is_click(faqs.readYaml('$.Activate.comment.input.submit'), s=0)

    def assert_input_error(self, name_class, email_class, context_class):
        class_name = self.getAttribute(faqs.readYaml('$.Activate.comment.input.name'), 'class', 0)
        class_email = self.getAttribute(faqs.readYaml('$.Activate.comment.input.email'), 'class', 0)
        class_context = self.getAttribute(faqs.readYaml('$.Activate.comment.input.context'), 'class', 0)
        self.allure_assert('判断数据格式错误提交评论', ('eq', class_name, name_class), ('eq', class_email, email_class),
                           ("eq", class_context, context_class))

    def assert_input_succeed_data(self, name, context):
        date = str(datetime.datetime.now().utcnow().strftime('%Y-%m-%d'))
        self.allure_assert('判断用户名提交评论成功',
                           ('eq', self.element_text(faqs.readYaml('$.Activate.comment.reviewer.name')), name),
                           ('include', date, self.element_text(faqs.readYaml('$.Activate.comment.reviewer.date'))),
                           ('eq', self.element_text(faqs.readYaml('$.Activate.comment.reviewer.context')), context),
                           ('eq', self.element_text(faqs.readYaml('$.Activate.comment.comment-num')), '1'))

    @allure.step('点击底部栏下载按钮')
    def click_sidebar_bottom(self):
        self.is_click(faqs.readYaml('$.Activate.comment.sidebar-bottom.download'))

    @allure.step('滑动到文章栏')
    def scroll_article(self):
        self.scroll_to_loc(faqs.readYaml('$.Activate.comment.article.index'))

    @allure.step('点击底部第一篇文章')
    def click_bottom_article_one(self):
        self.is_click(faqs.readYaml('$.Activate.comment.article.one'))

    @allure.step('点击底部第二篇文章')
    def click_bottom_article_two(self):
        self.is_click(faqs.readYaml('$.Activate.comment.article.two'))

    @allure.step('点击底部第三篇文章')
    def click_bottom_article_three(self):
        self.is_click(faqs.readYaml('$.Activate.comment.article.three'))

    @allure.step('点击底部第四篇文章')
    def click_bottom_article_four(self):
        self.is_click(faqs.readYaml('$.Activate.comment.article.four'))

    def assert_goto_article_one(self):
        self.allure_assert('判断跳转第一篇文章页面', (
            'eq', self.get_current_url(), 'https://www.imymac.com/mac-cleaner/how-to-free-up-space-on-mac.html'))

    def assert_goto_article_two(self):
        self.allure_assert('判断跳转第二篇文章页面', (
            'eq', self.get_current_url(), 'https://www.imymac.com/mac-uninstaller/uninstall-apps-on-mac.html'))

    def assert_goto_article_three(self):
        self.allure_assert('判断跳转第三篇文章页面', (
            'eq', self.get_current_url(), 'https://www.imymac.com/mac-cleaner/best-mac-cleaner.html'))

    def assert_goto_article_four(self):
        self.allure_assert('判断跳转第四篇文章页面', (
            'eq', self.get_current_url(), 'https://www.imymac.com/mac-cleaner/how-to-speed-up-mac.html'))

    @allure.step('展开所有常见问题')
    def unfold_faqs(self):
        elements = self.find_elements(faqs.readYaml('$.faqs.fold'))
        for element in elements:
            self.scroll_to_element(element)
            element.click()

    @allure.step('折叠所有常见问题')
    def fold_faqs(self):
        elements = self.find_elements(faqs.readYaml('$.faqs.fold'))
        for element in elements:
            self.scroll_to_element(element)
            element.click()
            element.click()

    def assert_faqs_unfold(self):
        num = len(self.find_elements(faqs.readYaml('$.faqs.item-active')))
        self.allure_assert('判断常见问题是否展开', ('eq', self.getAttributes(faqs.readYaml('$.faqs.item-active'), 'class'), [
            'faqs-item-desc faqs-active'] * num))

    def assert_faqs_fold(self):
        num = len(self.find_elements(faqs.readYaml('$.faqs.item-active')))
        self.allure_assert('判断常见问题是否折叠', ('eq', self.getAttributes(faqs.readYaml('$.faqs.item-active'), 'class'), [
            'faqs-item-desc'] * num))
