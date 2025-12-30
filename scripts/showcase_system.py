import os
import sys

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

# 导入必要的模型
from django.db import models

# 导入应用模型
from users.models import User
from warehouse.models import Warehouse
from goods.models import Goods, InboundRecord, OutboundRecord

# 展示系统数据
print("=" * 60)
print("Django仓库管理系统 - 数据展示")
print("=" * 60)

# 展示用户数据
print("\n【用户数据】")
print("-" * 30)
users = User.objects.all()
for user in users:
    print(f"用户名: {user.username}, 邮箱: {user.email}, 管理员: {'是' if user.is_admin else '否'}")

# 展示仓库数据
print("\n【仓库数据】")
print("-" * 30)
warehouses = Warehouse.objects.all()
for warehouse in warehouses:
    goods_count = warehouse.goods_set.count()
    total_quantity = warehouse.goods_set.aggregate(total=models.Sum('quantity'))['total'] or 0
    print(f"仓库: {warehouse.name}, 货物种类: {goods_count}, 总库存: {total_quantity}")

# 展示货物数据
print("\n【货物数据】")
print("-" * 30)
goods_list = Goods.objects.select_related('warehouse').all()
for goods in goods_list:
    status = "充足" if goods.quantity > 50 else "偏少" if goods.quantity > 10 else "紧张" if goods.quantity > 0 else "无货"
    print(f"货物: {goods.name} ({goods.specification}), 库存: {goods.quantity}, 仓库: {goods.warehouse.name}, 状态: {status}")

# 展示最近入库记录
print("\n【最近入库记录】")
print("-" * 30)
inbound_records = InboundRecord.objects.select_related('goods').order_by('-inbound_date')[:5]
for record in inbound_records:
    print(f"{record.inbound_date.strftime('%Y-%m-%d %H:%M')} 入库 {record.goods.name} {record.quantity} 件")

# 展示最近出库记录
print("\n【最近出库记录】")
print("-" * 30)
outbound_records = OutboundRecord.objects.select_related('goods').order_by('-outbound_date')[:5]
for record in outbound_records:
    print(f"{record.outbound_date.strftime('%Y-%m-%d %H:%M')} 出库 {record.goods.name} {record.quantity} 件")

# 统计数据
print("\n【统计数据】")
print("-" * 30)
total_goods = Goods.objects.count()
total_quantity = Goods.objects.aggregate(total=models.Sum('quantity'))['total'] or 0
total_inbound = InboundRecord.objects.aggregate(total=models.Sum('quantity'))['quantity__sum'] or 0
total_outbound = OutboundRecord.objects.aggregate(total=models.Sum('quantity'))['quantity__sum'] or 0

print(f"货物种类: {total_goods} 种")
print(f"库存总量: {total_quantity} 件")
print(f"累计入库: {total_inbound} 件")
print(f"累计出库: {total_outbound} 件")

print("\n" + "=" * 60)
print("系统功能特点:")
print("1. 完整的用户认证系统")
print("2. 仓库和货物的增删改查")
print("3. 货物出入库流程控制")
print("4. 库存盘点功能")
print("5. 货物搜索功能")
print("6. 数据可视化报表")
print("=" * 60)

# URL信息
print("\n系统访问地址:")
print("-" * 30)
print("根页面: http://127.0.0.1:8000/")
print("仓库列表: http://127.0.0.1:8000/warehouse/list/")
print("货物列表: http://127.0.0.1:8000/goods/")
print("库存报表: http://127.0.0.1:8000/reports/stock/")
print("管理后台: http://127.0.0.1:8000/admin/")
print("\n登录信息: 用户名 admin, 密码 admin123")

# 导入必要的模型
from django.db import models