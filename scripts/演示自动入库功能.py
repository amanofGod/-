#!/usr/bin/env python
"""
演示货物创建时自动入库功能
"""
import os
import sys
import django

# 设置Django环境
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from django.contrib.auth.models import User
from goods.models import Goods, InboundRecord
from warehouse.models import Warehouse

def demo_auto_inbound():
    print("🎯 演示：货物创建时自动入库功能")
    print("=" * 60)
    
    # 检查必要的数据
    print("📋 检查系统数据...")
    
    # 检查用户
    if not User.objects.exists():
        print("❌ 没有用户，请先创建管理员账号")
        return
    
    # 检查仓库
    warehouses = Warehouse.objects.all()
    if not warehouses.exists():
        print("📦 创建演示仓库...")
        Warehouse.objects.create(
            name="主仓库",
            location="一楼",
            capacity=1000,
            manager="管理员"
        )
        print("✅ 演示仓库创建成功")
    
    warehouse = Warehouse.objects.first()
    admin_user = User.objects.filter(is_superuser=True).first()
    
    print(f"👤 管理员: {admin_user.username if admin_user else 'None'}")
    print(f"📦 仓库: {warehouse.name}")
    
    # 清理之前的演示数据
    print("\n🧹 清理之前的演示数据...")
    Goods.objects.filter(name__contains="演示").delete()
    print("✅ 清理完成")
    
    # 演示创建货物
    print("\n🔧 演示1：创建货物并设置初始入库数量")
    print("-" * 40)
    
    # 模拟表单数据
    goods_data = {
        'name': '演示货物-笔记本电脑',
        'specification': 'DELL-14Pro-16GB-512GB',
        'warehouse': warehouse
    }
    
    # 创建货物（模拟表单保存过程）
    goods = Goods.objects.create(**goods_data)
    initial_quantity = 50  # 模拟用户输入的初始入库数量
    
    # 自动创建入库记录（这是我们的核心功能）
    if initial_quantity > 0:
        inbound_record = InboundRecord.objects.create(
            goods=goods,
            quantity=initial_quantity
        )
        # 更新货物库存
        goods.quantity = initial_quantity
        goods.save()
        
        print(f"✅ 货物创建成功: {goods.name}")
        print(f"✅ 自动入库: {initial_quantity} 件")
        print(f"✅ 当前库存: {goods.quantity} 件")
    
    # 演示查看结果
    print("\n📊 演示2：查看入库记录")
    print("-" * 40)
    
    inbound_records = goods.inboundrecord_set.all()
    print(f"📋 入库记录数量: {inbound_records.count()} 条")
    
    for i, record in enumerate(inbound_records, 1):
        print(f"   {i}. {record.inbound_date.strftime('%Y-%m-%d %H:%M')} - 入库 {record.quantity} 件")
    
    # 演示对比
    print("\n🔄 演示3：对比修改前后的逻辑")
    print("-" * 40)
    print("❌ 修改前：")
    print("   - 添加货物时库存为0")
    print("   - 需要额外进行入库操作")
    print("   - 用户体验差，逻辑不合理")
    
    print("\n✅ 修改后：")
    print("   - 添加货物时直接设置初始入库数量")
    print("   - 自动创建入库记录")
    print("   - 用户体验好，逻辑符合实际")
    
    print("\n🎉 演示完成！")
    print("\n🌐 现在可以访问以下地址测试：")
    print("   http://127.0.0.1:8000/goods/list/")
    print("   点击'添加货物'按钮测试新功能")
    
    # 保留演示数据用于Web测试
    print(f"\n💡 演示数据已保留，可在Web界面中查看:")
    print(f"   货物: {goods.name}")
    print(f"   库存: {goods.quantity} 件")

if __name__ == '__main__':
    demo_auto_inbound()