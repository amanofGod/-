#!/usr/bin/env python
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 简单测试筛选功能...")

try:
    from reports.forms import ReportFilterForm
    from warehouse.models import Warehouse
    from goods.models import Goods
    
    print(f"仓库数量: {Warehouse.objects.count()}")
    print(f"货物数量: {Goods.objects.count()}")
    
    # 创建一些测试数据
    if Warehouse.objects.count() < 2:
        Warehouse.objects.get_or_create(name="仓库A", defaults={'address': 'A', 'contact_person': 'A', 'contact_phone': 'A'})
        Warehouse.objects.get_or_create(name="仓库B", defaults={'address': 'B', 'contact_person': 'B', 'contact_phone': 'B'})
    
    warehouses = Warehouse.objects.all()
    for i, wh in enumerate(warehouses):
        Goods.objects.get_or_create(
            name=f"货物{i+1}",
            defaults={
                'specification': f"规格{i+1}",
                'quantity': (i+1) * 20,
                'warehouse': wh
            }
        )
    
    print("测试数据准备完成")
    
    # 测试表单
    warehouses = Warehouse.objects.all()
    for warehouse in warehouses:
        print(f"\n测试筛选仓库: {warehouse.name} (ID: {warehouse.id})")
        
        # 测试表单验证
        form_data = {'warehouse': warehouse.id}
        form = ReportFilterForm(data=form_data)
        
        if form.is_valid():
            selected_warehouse = form.cleaned_data['warehouse']
            print(f"✅ 表单验证成功")
            print(f"   选中的仓库: {selected_warehouse.name}")
            
            # 测试筛选逻辑
            goods_count = Goods.objects.filter(warehouse=selected_warehouse).count()
            print(f"   该仓库的货物数量: {goods_count}")
            
        else:
            print(f"❌ 表单验证失败")
            print(f"   错误: {form.errors}")
    
    # 测试无筛选
    print(f"\n测试无筛选")
    form = ReportFilterForm(data={})
    if form.is_valid():
        warehouse = form.cleaned_data.get('warehouse')
        print(f"✅ 无筛选表单验证成功，仓库: {warehouse}")
    else:
        print(f"❌ 无筛选表单验证失败")
    
    print("\n🎉 筛选功能测试完成！")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()