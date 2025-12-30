#!/usr/bin/env python
import os
import sys
import django

# 添加项目路径
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from goods.models import Goods, InboundRecord, OutboundRecord
from warehouse.models import Warehouse
from django.db.models import Sum, Count
from datetime import datetime, timedelta

print("=== 报表数据测试 ===")

# 1. 库存报表数据
print("\n--- 库存报表数据 ---")
goods_data = Goods.objects.select_related('warehouse').all()
print(f"货物总数: {goods_data.count()}")
for goods in goods_data:
    print(f"  {goods.name}: {goods.quantity}件 (仓库: {goods.warehouse.name})")

# 2. 仓库报表数据
print("\n--- 仓库报表数据 ---")
warehouses = Warehouse.objects.annotate(
    goods_count=Count('goods'),
    total_quantity=Sum('goods__quantity')
).all()
for warehouse in warehouses:
    print(f"  {warehouse.name}: {warehouse.goods_count}种货物, 总计{warehouse.total_quantity or 0}件")

# 3. 出入库报表数据
print("\n--- 出入库报表数据 ---")
inbound_records = InboundRecord.objects.all()
outbound_records = OutboundRecord.objects.all()

total_inbound = inbound_records.aggregate(Sum('quantity'))['quantity__sum'] or 0
total_outbound = outbound_records.aggregate(Sum('quantity'))['quantity__sum'] or 0

print(f"总入库量: {total_inbound}件")
print(f"总出库量: {total_outbound}件")

print(f"\n--- 最近入库记录 ---")
for record in inbound_records.order_by('-inbound_date')[:5]:
    print(f"  {record.goods.name}: +{record.quantity}件 ({record.inbound_date.strftime('%m-%d %H:%i')})")

print(f"\n--- 最近出库记录 ---")
for record in outbound_records.order_by('-outbound_date')[:5]:
    print(f"  {record.goods.name}: -{record.quantity}件 ({record.outbound_date.strftime('%m-%d %H:%i')})")

# 4. 测试日期筛选
print("\n--- 测试日期筛选 ---")
end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)

filtered_inbound = inbound_records.filter(inbound_date__date__gte=start_date)
filtered_outbound = outbound_records.filter(outbound_date__date__gte=start_date)

print(f"过去30天入库记录: {filtered_inbound.count()}条")
print(f"过去30天出库记录: {filtered_outbound.count()}条")

print("\n=== 报表URL测试 ===")
print("库存报表: http://127.0.0.1:8000/reports/stock/")
print("出入库报表: http://127.0.0.1:8000/reports/inbound-outbound/")
print("仓库报表: http://127.0.0.1:8000/reports/warehouse/")