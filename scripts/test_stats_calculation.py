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
from goods.forms import GoodsSearchForm

print('=== 测试统计数据计算 ===')

# 1. 测试基础数据（不包含搜索）
print('\n--- 基础统计（无搜索）---')
goods_list = Goods.objects.select_related('warehouse').all()
total_goods = goods_list.count()
total_quantity = goods_list.aggregate(total=Sum('quantity'))['total'] or 0
print(f'货物种类: {total_goods}')
print(f'总库存量: {total_quantity}')

# 2. 测试搜索表单的影响
print('\n--- 测试搜索表单 ---')
# 模拟GET请求参数
from django.test import RequestFactory
factory = RequestFactory()

# 测试无搜索参数的请求
request = factory.get('/goods/')
form = GoodsSearchForm(request.GET)
print(f'表单是否有效: {form.is_valid()}')
if form.is_valid() and form.cleaned_data['search_term']:
    search_term = form.cleaned_data['search_term']
    goods_list = goods_list.filter(name__icontains=search_term)
    print(f'应用搜索: {search_term}')
else:
    print('无搜索条件')

# 重新计算统计
total_goods = goods_list.count()
total_quantity = goods_list.aggregate(total=Sum('quantity'))['total'] or 0
print(f'应用搜索后 - 货物种类: {total_goods}')
print(f'应用搜索后 - 总库存量: {total_quantity}')

# 3. 检查每个货物的详细信息
print('\n--- 详细货物信息 ---')
for goods in goods_list:
    print(f'ID: {goods.id}, 名称: {goods.name}, 数量: {goods.quantity}, 仓库: {goods.warehouse.name if goods.warehouse else "无"}')