import os
import sys
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

import django
django.setup()

from warehouse.models import Warehouse
from goods.models import Goods

print("仓库删除状态检查")
print("=" * 40)

warehouses = Warehouse.objects.all()
for warehouse in warehouses:
    goods_count = warehouse.goods_set.count()
    goods_list = warehouse.goods_set.all()
    
    print(f"\n仓库: {warehouse.name}")
    print(f"货物数量: {goods_count}")
    
    if goods_count > 0:
        print("状态: ❌ 不能删除")
        print("原因: 仓库下还有货物")
        for goods in goods_list:
            print(f"  - {goods.name} (库存: {goods.quantity})")
    else:
        print("状态: ✅ 可以删除")
        print("原因: 仓库为空")

print("\n仓库删除规则:")
print("- 只有空的仓库才能删除")
print("- 这是保护数据完整性的机制")