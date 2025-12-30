#!/usr/bin/env python

print("""
=== 快速创建出入库测试数据 ===

请按以下步骤操作：

1. 打开命令提示符
2. 切换到项目目录：
   cd "d:\\good\\ job\\study\\wk\\ks\\1\\warehouse_management_system"

3. 启动Django shell：
   python manage.py shell

4. 复制以下完整代码粘贴进去：

from goods.models import InboundRecord, OutboundRecord, Goods
from warehouse.models import Warehouse
from datetime import datetime, timedelta
import random

print("开始创建测试数据...")

# 获取货物和仓库
goods_list = Goods.objects.all()
warehouses = Warehouse.objects.all()

print(f"找到 {len(goods_list)} 种货物")
print(f"找到 {len(warehouses)} 个仓库")

# 创建入库记录
print("\\n创建入库记录...")
for i in range(25):
    goods = random.choice(goods_list)
    quantity = random.randint(10, 80)
    date = datetime.now() - timedelta(days=random.randint(0, 15))
    
    record = InboundRecord.objects.create(
        goods=goods,
        quantity=quantity,
        inbound_date=date
    )
    print(f"  {goods.name}: +{quantity}件 ({date.strftime('%m-%d')})")

# 创建出库记录  
print("\\n创建出库记录...")
for i in range(20):
    goods = random.choice(goods_list)
    quantity = random.randint(5, 40)
    date = datetime.now() - timedelta(days=random.randint(0, 15))
    
    record = OutboundRecord.objects.create(
        goods=goods,
        quantity=quantity,
        outbound_date=date
    )
    print(f"  {goods.name}: -{quantity}件 ({date.strftime('%m-%d')})")

print(f"\\n=== 数据创建完成 ===")
print(f"入库记录: {InboundRecord.objects.count()}条")
print(f"出库记录: {OutboundRecord.objects.count()}条")

print("\\n现在刷新报表页面即可看到图表数据！")
print("出入库报表: http://127.0.0.1:8000/reports/inbound-outbound/")

5. 输入 exit() 退出shell

""")

input("按回车键退出...")