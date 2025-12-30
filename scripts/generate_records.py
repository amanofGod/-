import os
import sys

print("""
=== 生成测试出入库数据脚本 ===

请在Django shell中执行以下命令：

1. 打开命令提示符，切换到项目目录：
   cd "d:\\good\\ job\\study\\wk\\ks\\1\\warehouse_management_system"

2. 启动Django shell：
   python manage.py shell

3. 复制粘贴以下代码：

from goods.models import InboundRecord, OutboundRecord, Goods
from datetime import datetime, timedelta
import random

# 获取所有货物
goods_list = list(Goods.objects.all())
print(f'找到 {len(goods_list)} 种货物')

# 创建测试入库记录
print('创建入库记录...')
for i in range(10):
    goods = random.choice(goods_list)
    quantity = random.randint(10, 50)
    date = datetime.now() - timedelta(days=random.randint(0, 7))
    
    record = InboundRecord.objects.create(
        goods=goods,
        quantity=quantity,
        inbound_date=date
    )
    print(f'  {goods.name}: +{quantity}件')

# 创建测试出库记录
print('创建出库记录...')
for i in range(8):
    goods = random.choice(goods_list)
    quantity = random.randint(5, 30)
    date = datetime.now() - timedelta(days=random.randint(0, 7))
    
    record = OutboundRecord.objects.create(
        goods=goods,
        quantity=quantity,
        outbound_date=date
    )
    print(f'  {goods.name}: -{quantity}件')

print(f'\\n数据创建完成！')
print(f'入库记录: {InboundRecord.objects.count()}条')
print(f'出库记录: {OutboundRecord.objects.count()}条')

4. 输入 exit() 退出shell

然后刷新报表页面即可看到图表数据！
""")

input("按回车键退出...")