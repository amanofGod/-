#!/usr/bin/env python
import os
import sys
import django

# 添加项目路径
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from goods.models import InboundRecord, OutboundRecord, Goods
from datetime import datetime, timedelta
import random

print('=== 当前出入库数据 ===')
print(f'入库记录: {InboundRecord.objects.count()}条')
print(f'出库记录: {OutboundRecord.objects.count()}条')

if InboundRecord.objects.count() == 0:
    print('\n创建测试出入库数据...')
    goods_list = list(Goods.objects.all())
    
    if goods_list:
        # 创建过去10天的入库记录
        for i in range(20):
            goods = random.choice(goods_list)
            quantity = random.randint(10, 100)
            date = datetime.now() - timedelta(days=random.randint(0, 10))
            
            record = InboundRecord.objects.create(
                goods=goods,
                quantity=quantity,
                inbound_date=date
            )
            record.inbound_date = date
            record.save()
        
        # 创建过去10天的出库记录
        for i in range(15):
            goods = random.choice(goods_list)
            quantity = random.randint(5, 50)
            date = datetime.now() - timedelta(days=random.randint(0, 10))
            
            record = OutboundRecord.objects.create(
                goods=goods,
                quantity=quantity,
                outbound_date=date
            )
            record.outbound_date = date
            record.save()
        
        print('测试数据创建完成！')
        
print(f'\n=== 更新后数据 ===')
print(f'入库记录: {InboundRecord.objects.count()}条')
print(f'出库记录: {OutboundRecord.objects.count()}条')

print('\n=== 显示最近几条记录 ===')
for record in InboundRecord.objects.order_by('-inbound_date')[:3]:
    print(f'入库: {record.goods.name} {record.quantity}件 ({record.inbound_date.strftime("%m-%d %H:%i")})')

for record in OutboundRecord.objects.order_by('-outbound_date')[:3]:
    print(f'出库: {record.goods.name} {record.quantity}件 ({record.outbound_date.strftime("%m-%d %H:%i")})')