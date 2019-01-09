from airtest.cli.runner import AirtestCase, run_script
from argparse import *
from traceback import print_exc
import airtest.report.report as report
import jinja2
import shutil
import os
import io
import time
import allcase_list  # 调用数组文件
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
alltestnames = allcase_list.case_list()
print(alltestnames)
logger.info(alltestnames)


class CustomAirtestCase(AirtestCase):
    def setUp(self):
        print("custom setup")
        # add var/function/class/.. to globals
        # self.scope["hunter"] = "i am hunter"
        # self.scope["add"] = lambda x: x+1

        # exec setup script
        # self.exec_other_script("setup.owl")
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        # exec teardown script
        # self.exec_other_script("teardown.owl")
        super(CustomAirtestCase, self).setUp()

    def run_air(self, root_dir='D:\\tools\\airtestCase\\案例集', device=['android://127.0.0.1:5037/99.12.74.40:7281']):
        # 聚合结果
        results = []
        # 获取所有用例集
        root_log = root_dir + '\\' + 'log'
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)
            print('log文件夹位置=' + str(root_log))
        for f in alltestnames:
            if f.endswith(".air"):
                # f为.air案例名称：手机银行.air
                airName = f
                script = os.path.join(root_dir, f)
                # airName_path为.air的全路径：D:\tools\airtestCase\案例集\log\手机银行
                print('执行用例全路径='+script)
                # 日志存放路径和名称：D:\tools\airtestCase\案例集\log\手机银行1
                log = os.path.join(root_dir, 'log' + '\\' + airName.replace('.air', ''))
                print('用例log保存文件夹=' + log)
                if os.path.isdir(log):
                    shutil.rmtree(log)
                else:
                    os.makedirs(log)
                    print('log保存路径=' + str(root_log))
                output_file = log + '\\' + 'log.html'
                args = Namespace(device=device, log=log, recording=None, script=script)
                try:
                    run_script(args, AirtestCase)
                except:
                    # 创建一个日志器logger
                    logger.info(print_exc()) # 打印出异常
                    pass
                finally:
                    rpt = report.LogToHtml(script, log)
                    rpt.report("log_template.html", output_file=output_file)
                    result = {}
                    result["name"] = airName.replace('.air', '')
                    result["result"] = rpt.test_result
                    results.append(result)
        # 生成聚合报告
        root_dir_summary = 'E:\\AirtestCase\\SmartPOS-Old\\summary-log'
        print(root_dir)
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root_dir_summary),
            extensions=(),
            autoescape=True
        )
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        summary_name=now+"summary.html"

        template = env.get_template("summary_template.html", root_dir_summary)
        html = template.render({"results": results})
        output_file = os.path.join(root_dir_summary, summary_name)
        print('summary全路径=' + output_file)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)


if __name__ == '__main__':
    test = CustomAirtestCase()
    device = ['android:2d87aa41']
    # device = ['android:127.0.0.1:62001']
    test.run_air('E:\\AirtestCase\\SmartPOS-Old\\用例集', device)
