import os
import sys
import random

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

# 导入模型
from users.models import User
from warehouse.models import Warehouse
from goods.models import Goods, InboundRecord, OutboundRecord

# 创建测试数据
print("创建测试数据...")

# 创建仓库
warehouse_names = ["主仓库", "分仓库A", "分仓库B", "临时仓库"]
warehouse_contacts = ["张三", "李四", "王五", "赵六"]
warehouse_phones = ["13800138000", "13900139000", "13700137000", "13600136000"]

warehouses = []
for i in range(4):
    warehouse, created = Warehouse.objects.get_or_create(
        name=warehouse_names[i],
        defaults={
            "address": f"测试地址{i+1}号",
            "contact_person": warehouse_contacts[i],
            "contact_phone": warehouse_phones[i]
        }
    )
    warehouses.append(warehouse)
    if created:
        print(f"创建仓库: {warehouse.name}")

# 创建货物
goods_names = ["笔记本电脑", "显示器", "键盘", "鼠标", "打印机", "投影仪", "路由器", "交换机"]
goods_specs = ["ThinkPad X1", "27寸4K", "机械键盘", "无线鼠标", "激光打印机", "高清投影仪", "千兆路由器", "24口交换机"]

goods = []
for i, name in enumerate(goods_names):
    goods_item, created = Goods.objects.get_or_create(
        name=name,
        defaults={
            "specification": goods_specs[i],
            "quantity": random.randint(10, 100),
            "warehouse": random.choice(warehouses)
        }
    )
    goods.append(goods_item)
    if created:
        print(f"创建货物: {goods_item.name}")

# 创建入库记录
for goods_item in goods:
    for _ in range(random.randint(2, 5)):
        InboundRecord.objects.create(
            goods=goods_item,
            quantity=random.randint(5, 50)
        )

# 创建出库记录
for goods_item in goods:
    for _ in range(random.randint(1, 3)):
        OutboundRecord.objects.create(
            goods=goods_item,
            quantity=random.randint(3, 20)
        )

print("测试数据创建完成！")
print(f"已创建 {Warehouse.objects.count()} 个仓库")
print(f"已创建 {Goods.objects.count()} 种货物")
print(f"已创建 {InboundRecord.objects.count()} 条入库记录")
print(f"已创建 {OutboundRecord.objects.count()} 条出库记录")