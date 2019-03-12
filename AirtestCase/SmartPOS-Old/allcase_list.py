# untie执行用例列表

# shop执行用例列表
def case_list():
    alltestnames = [
        # '简餐-下单-打包费.air',
        # '简餐-下单-会员支付.air',
        # '简餐-下单-属性_价格增加-其它.air',
        # '正餐-桌台-餐具费-下单-清台.air',
        '场景一-奶茶店模式.air',
        '场景二-反结账.air',
        '场景二-反结账-继续点餐.air',
        '场景四-正餐-移台-结账-清台.air',
        '场景五-现金-找零',
        '场景六-混合支付.air',
    ]
    return alltestnames


# 目前存在问题alltestnames有一个用例，设置循环多次会报错，进程被占用
def loop_num():
    loop_num = 1
    return loop_num
