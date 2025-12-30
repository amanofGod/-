#!/usr/bin/env python
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from warehouse.models import Warehouse
from goods.models import Goods, InboundRecord, OutboundRecord
from datetime import datetime, timedelta

def test_reports():
    """测试报表功能"""
    print("🧪 开始测试报表功能...")
    
    # 创建测试用户
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com', 'is_active': True}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("✅ 创建测试用户")
    
    # 创建测试仓库
    warehouse, created = Warehouse.objects.get_or_create(
        name='测试仓库',
        defaults={
            'address': '测试地址',
            'capacity': 1000,
            'description': '测试用仓库'
        }
    )
    if created:
        print("✅ 创建测试仓库")
    
    # 创建测试货物
    goods, created = Goods.objects.get_or_create(
        name='测试货物',
        defaults={
            'warehouse': warehouse,
            'quantity': 100,
            'unit': '个',
            'min_quantity': 10
        }
    )
    if created:
        print("✅ 创建测试货物")
    
    # 创建出入库记录
    today = datetime.now()
    
    # 入库记录
    for i in range(5):
        date = today - timedelta(days=i)
        InboundRecord.objects.get_or_create(
            goods=goods,
            inbound_date=date,
            defaults={
                'quantity': 10 + i,
                'operator': '测试用户',
                'remarks': f'测试入库{i}'
            }
        )
    
    # 出库记录
    for i in range(3):
        date = today - timedelta(days=i)
        OutboundRecord.objects.get_or_create(
            goods=goods,
            outbound_date=date,
            defaults={
                'quantity': 5 + i,
                'operator': '测试用户',
                'remarks': f'测试出库{i}'
            }
        )
    
    print("✅ 创建测试数据")
    
    # 测试报表视图
    from reports.views import (
        stock_report_view,
        warehouse_report_view, 
        inbound_report_view,
        outbound_report_view,
        inbound_outbound_report_view
    )
    
    # 创建模拟请求
    from django.http import HttpRequest
    from django.contrib.auth.models import AnonymousUser
    
    request = HttpRequest()
    request.user = user
    request.method = 'GET'
    request.GET = {}
    
    try:
        # 测试库存报表
        response = stock_report_view(request)
        print("✅ 库存报表视图测试通过")
        
        # 测试仓库报表
        response = warehouse_report_view(request)
        print("✅ 仓库报表视图测试通过")
        
        # 测试入库报表
        response = inbound_report_view(request)
        print("✅ 入库报表视图测试通过")
        
        # 测试出库报表
        response = outbound_report_view(request)
        print("✅ 出库报表视图测试通过")
        
        # 测试综合报表
        response = inbound_outbound_report_view(request)
        print("✅ 综合出入库报表视图测试通过")
        
    except Exception as e:
        print(f"❌ 报表视图测试失败: {e}")
        return False
    
    print("🎉 所有报表功能测试完成！")
    return True

if __name__ == '__main__':
    test_reports()