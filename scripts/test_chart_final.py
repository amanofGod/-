import os, sys
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')

print("🧪 运行Django测试...")
os.system('python manage.py shell -c """
from django.test import RequestFactory
from django.contrib.auth.models import User
from reports.views import stock_report_view
from warehouse.models import Warehouse
from goods.models import Goods
import json

# 确保有数据
if Warehouse.objects.count() == 0:
    w1 = Warehouse.objects.create(name=\"仓库A\", address=\"A\", contact_person=\"A\", contact_phone=\"A\")
    w2 = Warehouse.objects.create(name=\"仓库B\", address=\"B\", contact_person=\"B\", contact_phone=\"B\")
    Goods.objects.create(name=\"货物1\", specification=\"规格1\", quantity=50, warehouse=w1)
    Goods.objects.create(name=\"货物2\", specification=\"规格2\", quantity=30, warehouse=w1) 
    Goods.objects.create(name=\"货物3\", specification=\"规格3\", quantity=70, warehouse=w2)
    print(\"创建了测试数据\")

# 测试用户
user = User.objects.first() or User.objects.create_user(\"test\", \"test@example.com\", \"test\")
factory = RequestFactory()

# 无筛选测试
request = factory.get(\"/reports/stock/\")
request.user = user
response = stock_report_view(request)
chart_data = json.loads(response.context_data[\"chart_data\"])

print(\"无筛选图表数据:\")
print(f\"  labels: {chart_data.get(\"labels\", [])}\")
print(f\"  data: {chart_data.get(\"data\", [])}\")

# 筛选测试
w1 = Warehouse.objects.first()
request = factory.get(f\"/reports/stock/?warehouse={w1.id}\")
request.user = user
response = stock_report_view(request)
chart_data = json.loads(response.context_data[\"chart_data\"])

print(\"筛选后图表数据:\")
print(f\"  labels: {chart_data.get(\"labels\", [])}\")
print(f\"  data: {chart_data.get(\"data\", [])}\")
print(\"✅ 图表筛选测试完成\")
""")