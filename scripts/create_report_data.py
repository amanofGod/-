#!/usr/bin/env python

import os
import sys
import django

# 添加Django项目路径
project_path = r'd:\good job\study\wk\ks\1\warehouse_management_system'
sys.path.insert(0, project_path)
os.chdir(project_path)

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

try:
    from goods.models import InboundRecord, OutboundRecord, Goods
    from warehouse.models import Warehouse
    from datetime import datetime, timedelta
    import random
    
    print("=== 生成出入库报表数据 ===")
    
    # 检查现有数据
    goods_count = Goods.objects.count()
    warehouse_count = Warehouse.objects.count()
    inbound_count = InboundRecord.objects.count()
    outbound_count = OutboundRecord.objects.count()
    
    print(f"当前数据状态:")
    print(f"  货物: {goods_count}种")
    print(f"  仓库: {warehouse_count}个")
    print(f"  入库记录: {inbound_count}条")
    print(f"  出库记录: {outbound_count}条")
    
    if goods_count == 0 or warehouse_count == 0:
        print("\n错误：没有货物或仓库数据！请先创建货物和仓库。")
        return
    
    if inbound_count < 10 or outbound_count < 10:
        print(f"\n生成测试数据...")
        
        goods_list = list(Goods.objects.all())
        
        # 生成更多入库记录
        for i in range(30):
            goods = random.choice(goods_list)
            quantity = random.randint(20, 100)
            date = datetime.now() - timedelta(days=random.randint(0, 20))
            
            InboundRecord.objects.get_or_create(
                goods=goods,
                quantity=quantity,
                inbound_date=date
            )
        
        # 生成更多出库记录
        for i in range(25):
            goods = random.choice(goods_list)
            quantity = random.randint(10, 60)
            date = datetime.now() - timedelta(days=random.randint(0, 20))
            
            OutboundRecord.objects.get_or_create(
                goods=goods,
                quantity=quantity,
                outbound_date=date
            )
        
        print("✅ 测试数据创建完成！")
        
    # 显示最终统计
    final_inbound = InboundRecord.objects.count()
    final_outbound = OutboundRecord.objects.count()
    
    print(f"\n=== 最终数据 ===")
    print(f"入库记录: {final_inbound}条")
    print(f"出库记录: {final_outbound}条")
    
    if final_inbound > 0 and final_outbound > 0:
        print("\n🎉 现在可以访问报表页面查看图表了！")
        print("出入库报表: http://127.0.0.1:8000/reports/inbound-outbound/")
    else:
        print("\n❌ 数据创建失败，请检查错误信息")

except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()

input("\n按回车键退出...")