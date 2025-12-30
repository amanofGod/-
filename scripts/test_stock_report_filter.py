#!/usr/bin/env python
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 测试库存报表筛选功能...")

try:
    from django.test import RequestFactory
    from django.contrib.auth.models import User
    from reports.views import stock_report_view
    from warehouse.models import Warehouse
    from goods.models import Goods
    
    # 检查数据
    print(f"仓库数量: {Warehouse.objects.count()}")
    print(f"货物数量: {Goods.objects.count()}")
    
    if Warehouse.objects.count() == 0:
        print("❌ 没有仓库数据，创建测试数据...")
        Warehouse.objects.create(name="测试仓库1", address="地址1", contact_person="联系人1", contact_phone="电话1")
        Warehouse.objects.create(name="测试仓库2", address="地址2", contact_person="联系人2", contact_phone="电话2")
        print("✅ 创建了测试仓库")
    
    if Goods.objects.count() == 0:
        print("❌ 没有货物数据，创建测试货物...")
        warehouses = Warehouse.objects.all()
        for i, warehouse in enumerate(warehouses):
            Goods.objects.create(
                name=f"测试货物{i+1}",
                specification=f"规格{i+1}",
                quantity=50 + i * 10,
                warehouse=warehouse
            )
        print("✅ 创建了测试货物")
    
    # 创建测试用户
    user = User.objects.first() or User.objects.create_user('test', 'test@example.com', 'test')
    
    # 创建模拟请求
    factory = RequestFactory()
    
    # 测试无筛选的请求
    print("\n📊 测试1: 无筛选")
    request = factory.get('/reports/stock/')
    request.user = user
    
    try:
        response = stock_report_view(request)
        print(f"✅ 无筛选请求成功，状态码: {response.status_code}")
        context = response.context_data
        print(f"   - 仓库数量: {context['total_warehouses']}")
        print(f"   - 货物种类: {context['total_goods_count']}")
        print(f"   - 库存总量: {context['total_quantity']}")
    except Exception as e:
        print(f"❌ 无筛选请求失败: {e}")
    
    # 测试按仓库筛选
    if Warehouse.objects.exists():
        first_warehouse = Warehouse.objects.first()
        print(f"\n📊 测试2: 筛选仓库 '{first_warehouse.name}'")
        request = factory.get(f'/reports/stock/?warehouse={first_warehouse.id}')
        request.user = user
        
        try:
            response = stock_report_view(request)
            print(f"✅ 筛选请求成功，状态码: {response.status_code}")
            context = response.context_data
            print(f"   - 仓库数量: {context['total_warehouses']}")
            print(f"   - 货物种类: {context['total_goods_count']}")
            print(f"   - 库存总量: {context['total_quantity']}")
            
            # 检查筛选后的数据
            warehouse_goods_data = context['warehouse_goods_data']
            print(f"   - 筛选后仓库数量: {len(warehouse_goods_data)}")
            for wh, data in warehouse_goods_data.items():
                print(f"     * {wh.name}: {data['goods_count']} 种货物，总量 {data['quantity']}")
                
        except Exception as e:
            print(f"❌ 筛选请求失败: {e}")
    
    print("\n🎉 库存报表筛选功能测试完成！")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()