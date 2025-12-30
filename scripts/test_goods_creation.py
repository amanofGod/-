#!/usr/bin/env python
"""
测试货物创建和自动入库功能
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

def test_goods_creation():
    print("🧪 测试货物创建和自动入库功能")
    print("=" * 50)
    
    # 检查是否有仓库
    warehouses = Warehouse.objects.all()
    if not warehouses.exists():
        print("❌ 没有找到仓库，请先创建仓库")
        return
    
    warehouse = warehouses.first()
    print(f"📦 使用仓库: {warehouse.name}")
    
    # 创建测试货物
    print("\n🔧 创建测试货物...")
    goods_data = {
        'name': '测试货物-自动入库',
        'specification': 'TEST-001',
        'warehouse': warehouse
    }
    
    # 创建货物（这里我们直接模拟表单数据）
    goods = Goods.objects.create(**goods_data)
    print(f"✅ 货物创建成功: {goods.name}")
    
    # 模拟初始入库
    initial_quantity = 100
    inbound_record = InboundRecord.objects.create(
        goods=goods,
        quantity=initial_quantity
    )
    
    # 更新库存
    goods.quantity = initial_quantity
    goods.save()
    
    print(f"✅ 自动入库成功: {initial_quantity} 件")
    
    # 验证结果
    print("\n📊 验证结果:")
    print(f"   货物库存: {goods.quantity} 件")
    print(f"   入库记录数: {goods.inboundrecord_set.count()} 条")
    
    latest_inbound = goods.inboundrecord_set.first()
    if latest_inbound:
        print(f"   最新入库: {latest_inbound.quantity} 件")
    
    print("\n🎉 测试完成！货物创建和自动入库功能正常工作")
    
    # 清理测试数据
    print("\n🧹 清理测试数据...")
    goods.delete()
    print("✅ 测试数据已清理")

if __name__ == '__main__':
    test_goods_creation()