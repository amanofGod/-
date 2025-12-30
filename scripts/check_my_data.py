#!/usr/bin/env python
import os, sys, django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 检查你的本地数据库...")
print(f"数据库文件位置: d:\\good job\\study\\wk\\ks\\1\\warehouse_management_system\\db.sqlite3")

try:
    from warehouse.models import Warehouse
    from goods.models import Goods, InboundRecord, OutboundRecord
    from django.contrib.auth.models import User
    
    print(f"\n📊 数据统计:")
    print(f"👥 用户数量: {User.objects.count()}")
    print(f"🏢 仓库数量: {Warehouse.objects.count()}")
    print(f"📦 货物数量: {Goods.objects.count()}")
    print(f"📥 入库记录: {InboundRecord.objects.count()}")
    print(f"📤 出库记录: {OutboundRecord.objects.count()}")
    
    # 详细信息
    if Warehouse.objects.exists():
        print(f"\n🏢 仓库列表:")
        for wh in Warehouse.objects.all():
            goods_count = Goods.objects.filter(warehouse=wh).count()
            total_quantity = Goods.objects.filter(warehouse=wh).aggregate(total=models.Sum('quantity'))['total'] or 0
            print(f"  📁 {wh.name}: {goods_count} 种货物，总量 {total_quantity}")
    
    if Goods.objects.exists():
        print(f"\n📦 货物列表 (前10个):")
        for goods in Goods.objects.all()[:10]:
            print(f"  📦 {goods.name} ({goods.warehouse.name}): {goods.quantity} 件")
    
    if User.objects.exists():
        print(f"\n👥 用户列表:")
        for user in User.objects.all():
            is_active = "✅ 活跃" if user.is_active else "❌ 未激活"
            print(f"  👤 {user.username} - {is_active}")
    
    print(f"\n✅ 数据库检查完成！你的所有数据都安全保存在本地SQLite文件中。")
    
except ImportError as e:
    print(f"❌ 模块导入失败: {e}")
except Exception as e:
    print(f"❌ 数据库检查失败: {e}")
    import traceback
    traceback.print_exc()