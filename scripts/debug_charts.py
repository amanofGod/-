import os, sys, json
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import User
from reports.views import stock_report_view
from warehouse.models import Warehouse
from goods.models import Goods

# 创建测试数据
if Warehouse.objects.count() == 0:
    w1 = Warehouse.objects.create(name='仓库A', address='A', contact_person='A', contact_phone='A')
    w2 = Warehouse.objects.create(name='仓库B', address='B', contact_person='B', contact_phone='B')
    
    Goods.objects.create(name='货物A1', specification='规格A1', quantity=50, warehouse=w1)
    Goods.objects.create(name='货物A2', specification='规格A2', quantity=30, warehouse=w1)
    Goods.objects.create(name='货物B1', specification='规格B1', quantity=70, warehouse=w2)

user = User.objects.first() or User.objects.create_user('test', 'test@example.com', 'test')
factory = RequestFactory()

print("🔍 调试图表数据...")

# 测试无筛选
print("\n1. 无筛选测试:")
request = factory.get('/reports/stock/')
request.user = user
response = stock_report_view(request)

chart_data_str = response.context_data['chart_data']
print(f"原始chart_data类型: {type(chart_data_str)}")
print(f"原始chart_data长度: {len(chart_data_str)}")
print(f"原始chart_data前100字符: {chart_data_str[:100]}")

try:
    chart_data = json.loads(chart_data_str)
    print(f"解析成功:")
    print(f"  labels: {chart_data.get('labels', [])}")
    print(f"  data: {chart_data.get('data', [])}")
except Exception as e:
    print(f"JSON解析失败: {e}")

# 测试筛选
print("\n2. 筛选测试:")
w1 = Warehouse.objects.first()
request = factory.get(f'/reports/stock/?warehouse={w1.id}')
request.user = user
response = stock_report_view(request)

chart_data_str = response.context_data['chart_data']
print(f"筛选后chart_data前100字符: {chart_data_str[:100]}")

try:
    chart_data = json.loads(chart_data_str)
    print(f"筛选后解析成功:")
    print(f"  labels: {chart_data.get('labels', [])}")
    print(f"  data: {chart_data.get('data', [])}")
except Exception as e:
    print(f"筛选后JSON解析失败: {e}")

print("\n✅ 调试完成")