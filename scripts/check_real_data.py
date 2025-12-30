#!/usr/bin/env python
import os
import sys
import django

# 添加项目路径
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from goods.models import Goods
from django.db.models import Sum

print('=== 货物数据 ===')
goods_list = Goods.objects.all()
for g in goods_list:
    print(f'ID: {g.id}, 名称: {g.name}, 数量: {g.quantity}')

total = Goods.objects.aggregate(total=Sum('quantity'))['total'] or 0
print(f'实际总库存: {total}')

# 检查views.py中的计算逻辑
print('\n=== 检查views.py中的统计计算 ===')
# 模拟视图中的计算
total_goods = goods_list.count()
total_quantity = goods_list.aggregate(total=Sum('quantity'))['total'] or 0
low_stock_count = goods_list.filter(quantity__lte=10).count()
normal_stock_count = goods_list.filter(quantity__gt=50).count()

print(f'货物种类: {total_goods}')
print(f'总库存量: {total_quantity}')
print(f'库存预警: {low_stock_count}')
print(f'库存正常: {normal_stock_count}')