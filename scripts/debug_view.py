import os, sys, django, json
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import User
from reports.views import stock_report_view
from warehouse.models import Warehouse
from goods.models import Goods

print("🔍 直接测试视图...")

# 确保有数据
if Warehouse.objects.count() < 2:
    Warehouse.objects.create(name="仓库A", address="A", contact_person="A", contact_phone="A")
    Warehouse.objects.create(name="仓库B", address="B", contact_person="B", contact_phone="B")
    
warehouses = list(Warehouse.objects.all())
for i, wh in enumerate(warehouses):
    Goods.objects.get_or_create(
        name=f"货物{i+1}",
        defaults={
            'specification': f"规格{i+1}",
            'quantity': (i+1) * 20,
            'warehouse': wh
        }
    )

user = User.objects.first() or User.objects.create_user('test', 'test@example.com', 'test')
factory = RequestFactory()

print(f"有 {Warehouse.objects.count()} 个仓库, {Goods.objects.count()} 个货物")

# 测试筛选
w = warehouses[0]
print(f"测试筛选仓库: {w.name} (ID: {w.id})")

request = factory.get(f'/reports/stock/?warehouse={w.id}')
request.user = user
response = stock_report_view(request)

# 检查响应数据
context = response.context_data
chart_data_str = context.get('chart_data', '{}')
print(f"chart_data_str: {chart_data_str[:100]}...")

try:
    chart_data = json.loads(chart_data_str)
    print(f"解析成功的chart_data:")
    print(f"  labels: {chart_data.get('labels', [])}")
    print(f"  data: {chart_data.get('data', [])}")
    print(f"  labels数量: {len(chart_data.get('labels', []))}")
    print(f"  data数量: {len(chart_data.get('data', []))}")
    
    if len(chart_data.get('labels', [])) == 1 and chart_data.get('labels', [''])[0] == w.name:
        print("✅ 图表数据筛选正确！")
    else:
        print("❌ 图表数据筛选有问题！")
        
except json.JSONDecodeError as e:
    print(f"❌ JSON解析失败: {e}")
    print(f"原始字符串: {chart_data_str}")

print("\n🎉 调试完成！")