#!/usr/bin/env python
import os
import sys
import json
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 测试图表数据更新...")

try:
    from django.test import RequestFactory
    from django.contrib.auth.models import User
    from reports.views import stock_report_view
    from warehouse.models import Warehouse
    from goods.models import Goods
    
    # 创建测试数据
    if Warehouse.objects.count() == 0:
        Warehouse.objects.create(name="仓库A", address="A", contact_person="A", contact_phone="A")
        Warehouse.objects.create(name="仓库B", address="B", contact_person="B", contact_phone="B")
        print("✅ 创建了测试仓库")
    
    warehouses = Warehouse.objects.all()
    for i, wh in enumerate(warehouses):
        Goods.objects.get_or_create(
            name=f"货物{i+1}",
            defaults={
                'specification': f"规格{i+1}",
                'quantity': (i+1) * 50,
                'warehouse': wh
            }
        )
    
    print("✅ 创建了测试货物")
    
    # 创建测试用户
    user = User.objects.first() or User.objects.create_user('test', 'test@example.com', 'test')
    factory = RequestFactory()
    
    # 测试无筛选的图表数据
    print("\n📊 测试1: 无筛选的图表数据")
    request = factory.get('/reports/stock/')
    request.user = user
    
    response = stock_report_view(request)
    context = response.context_data
    chart_data_str = context.get('chart_data', '{}')
    
    print(f"✅ 图表数据长度: {len(chart_data_str)} 字符")
    
    # 解析JSON数据
    chart_data = json.loads(chart_data_str)
    print(f"   - 图表标签数量: {len(chart_data.get('labels', []))}")
    print(f"   - 数据点数量: {len(chart_data.get('data', []))}")
    print(f"   - 标签: {chart_data.get('labels', [])}")
    print(f"   - 数据: {chart_data.get('data', [])}")
    
    # 测试按仓库筛选的图表数据
    if warehouses.exists():
        first_warehouse = warehouses.first()
        print(f"\n📊 测试2: 筛选仓库 '{first_warehouse.name}' 的图表数据")
        request = factory.get(f'/reports/stock/?warehouse={first_warehouse.id}')
        request.user = user
        
        response = stock_report_view(request)
        context = response.context_data
        chart_data_str = context.get('chart_data', '{}')
        
        chart_data = json.loads(chart_data_str)
        print(f"✅ 筛选后图表数据:")
        print(f"   - 图表标签数量: {len(chart_data.get('labels', []))}")
        print(f"   - 数据点数量: {len(chart_data.get('data', []))}")
        print(f"   - 标签: {chart_data.get('labels', [])}")
        print(f"   - 数据: {chart_data.get('data', [])}")
        
        # 验证筛选是否生效
        if len(chart_data.get('labels', [])) == 1 and chart_data.get('labels', [''])[0] == first_warehouse.name:
            print("✅ 图表筛选功能正常工作！")
        else:
            print("❌ 图表筛选功能有问题！")
    
    print("\n🎉 图表数据测试完成！")
    print("\n现在筛选报表时图表应该会动态更新了！")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()