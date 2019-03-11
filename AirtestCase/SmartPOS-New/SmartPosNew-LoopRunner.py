from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
import jinja2
import shutil
import os
import io
import time
import allcase_list  # 调用数组文件
import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger('root')
alltestnames = allcase_list.case_list()
loop_num = allcase_list.loop_num()  # 循环alltestnames次数
logger.info(alltestnames)
conf_root_dir = 'E:\\AirtestCase\\SmartPOS-New\\'


class CustomAirtestCase(AirtestCase):
    def setUp(self):
        logger.info("custom setup")
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        logger.info("custom tearDown")
        super(CustomAirtestCase, self).setUp()

    def run_air(self, root_dir='D:\\tools\\airtestCase\\案例集', device=['android://127.0.0.1:5037/99.12.74.40:7281']):
        # 聚合结果
        results = []
        case_count = 0
        case_count_success = 0
        case_count_fail = 0
        # 获取所有用例集
        root_log = root_dir + '\\' + 'log'
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)
            logger.info('log文件夹位置=' + str(root_log))
        for n in range(loop_num):
            n = n + 1
            logger.info("=========循环次数=" + str(n) + "================")
            for f in alltestnames:
                case_count = case_count + 1
                logger.info("========case_count=" + str(case_count) + "===========")
                if f.endswith(".air"):
                    # f为.air案例名称：手机银行.air
                    airName = f
                    script = os.path.join(root_dir, f)
                    # airName_path为.air的全路径：D:\tools\airtestCase\案例集\log\手机银行
                    logger.info('执行用例全路径=' + script)
                    # 日志存放路径和名称：D:\tools\airtestCase\案例集\log\手机银行1
                    log = os.path.join(root_dir, 'log' + '\\' + airName.replace('.air', ''))
                    logger.info('用例log保存文件夹=' + log)
                    if os.path.isdir(log):
                        shutil.rmtree(log)
                    else:
                        os.makedirs(log)
                        logger.info('log保存路径=' + str(root_log))
                    output_file = log + '\\' + 'log.html'
                    args = Namespace(device=device, log=log, recording=None, script=script)
                    try:
                        run_script(args, AirtestCase)
                    except:
                        pass
                    finally:
                        rpt = report.LogToHtml(script, log)
                        try:
                            rpt.report("log_template.html", output_file=output_file)
                        except Exception as e:
                            # 创建一个日志器logger
                            logger.exception(str(e))
                            pass
                        result = {}
                        result["name"] = airName.replace('.air', '')
                        result["result"] = rpt.test_result
                        if str(rpt.test_result) == 'True':
                            case_count_success = case_count_success + 1
                        else:
                            case_count_fail = case_count_fail + 1
                        result["conf_root_dir"] = conf_root_dir
                        results.append(result)

        # 生成聚合报告
        # root_dir_summary = conf_root_dir + 'summary-log'
        root_dir_summary = '../summary-log'
        logger.info(root_dir)
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root_dir_summary),
            extensions=(),
            autoescape=True
        )
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        summary_name = now + "summary_loop.html"

        template = env.get_template("summary_template_loop.html", root_dir_summary)
        html = template.render({"results": results}, case_count=case_count, case_count_success=case_count_success,
                               case_count_fail=case_count_fail)

        output_file = os.path.join(root_dir_summary, summary_name)
        logger.info('summary全路径=' + output_file)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)


if __name__ == '__main__':
    test = CustomAirtestCase()
    device = ['android:DB04D88900018']  # 商米D1s
    # device = ['android:2d87aa41']  # 商米D1
    # device = ['android:172.16.32.31:8888']#,'android:172.16.32.32:8888'
    for d in device:
        # print("d="+d)
        # device_ip = re.search("android:(.*):8888", d).group(1)  # 截取当前地址中的order_num
        # print('device_ip=' + device_ip)
        test.run_air(conf_root_dir + '用例集循环', d)
        # test.run_air(conf_root_dir + '用例集', device)
