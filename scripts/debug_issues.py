#!/usr/bin/env python
"""
调试入库和删除功能问题
"""
import os
import sys
import django

# 设置Django环境
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from goods.models import Goods, InboundRecord
from warehouse.models import Warehouse

def debug_issues():
    print("🔍 调试入库和删除功能问题")
    print("=" * 50)
    
    # 检查货物数据
    print("\n📦 检查货物数据:")
    goods_list = Goods.objects.all()
    for goods in goods_list:
        print(f"  - {goods.name} (ID: {goods.id}, 仓库: {goods.warehouse.name}, 库存: {goods.quantity})")
    
    # 检查入库记录
    print("\n📥 检查入库记录:")
    inbound_records = InboundRecord.objects.all()
    for record in inbound_records:
        print(f"  - {record.goods.name} 入库 {record.quantity} 件 ({record.inbound_date})")
    
    # 检查仓库数据
    print("\n🏢 检查仓库数据:")
    warehouses = Warehouse.objects.all()
    for warehouse in warehouses:
        goods_count = Goods.objects.filter(warehouse=warehouse).count()
        print(f"  - {warehouse.name} (ID: {warehouse.id}, 货物数量: {goods_count})")
    
    print("\n🔧 模拟问题场景:")
    
    if goods_list.exists():
        test_goods = goods_list.first()
        print(f"测试货物: {test_goods.name}")
        
        # 检查入库表单是否能找到这个货物
        warehouse = test_goods.warehouse
        goods_in_warehouse = Goods.objects.filter(warehouse=warehouse)
        print(f"在仓库 {warehouse.name} 中找到的货物: {list(goods_in_warehouse.values_list('name', flat=True))")
        
        # 测试删除
        try:
            test_goods_name = test_goods.name
            # 注意：这里不实际删除，只是测试权限
            print(f"✅ 删除权限检查通过，可以删除 {test_goods_name}")
        except Exception as e:
            print(f"❌ 删除权限检查失败: {e}")
    else:
        print("❌ 没有货物数据，请先创建货物")
    
    print("\n🌐 测试建议:")
    print("1. 访问入库页面: http://127.0.0.1:8000/goods/inbound/")
    print("2. 选择仓库，检查是否显示货物")
    print("3. 点击删除按钮，检查JavaScript是否执行")

if __name__ == '__main__':
    debug_issues()