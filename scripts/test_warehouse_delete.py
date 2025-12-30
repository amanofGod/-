import os
import sys

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

from warehouse.models import Warehouse
from goods.models import Goods

print("=" * 50)
print("仓库删除逻辑测试")
print("=" * 50)

warehouses = Warehouse.objects.all()

for warehouse in warehouses:
    goods_count = warehouse.goods_set.count()
    goods_list = warehouse.goods_set.all()
    
    print(f"\n仓库: {warehouse.name}")
    print(f"  联系人: {warehouse.contact_person}")
    print(f"  电话: {warehouse.contact_phone}")
    print(f"  货物种类: {goods_count}")
    
    if goods_count > 0:
        print(f"  ❌ 无法删除 - 还有 {goods_count} 种货物:")
        for goods in goods_list:
            print(f"     - {goods.name} (库存: {goods.quantity})")
        print(f"  删除提示: 必须先将所有货物转移到其他仓库或删除")
    else:
        print(f"  ✅ 可以删除 - 无货物")
        print(f"  删除提示: 可以安全删除此仓库")

print("\n" + "=" * 50)
print("删除逻辑说明:")
print("1. 如果仓库下有货物，系统会阻止删除并提示错误")
print("2. 这是保护数据完整性的设计，防止货物失去归属")
print("3. 只有完全空的仓库才能被删除")
print("=" * 50)

# 提供删除建议
print("\n操作建议:")
print("1. 先将某仓库下的货物转移到其他仓库")
print("2. 然后就可以删除空仓库了")
print("3. 或者使用级联删除（需要在数据库层面配置外键关系）")