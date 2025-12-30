#!/usr/bin/env python
"""
测试入库和删除功能
"""
import os
import sys
import django

# 设置Django环境
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from goods.models import Goods, InboundRecord
from warehouse.models import Warehouse

def test_functionality():
    print("🧪 测试入库和删除功能")
    print("=" * 50)
    
    # 创建测试客户端
    client = Client()
    
    # 检查用户
    user = User.objects.filter(username='admin').first()
    if not user:
        print("❌ 没有找到admin用户")
        return
    
    # 登录
    client.login(username='admin', password='admin123')
    print("✅ 已登录admin用户")
    
    # 检查仓库
    warehouse = Warehouse.objects.first()
    if not warehouse:
        print("❌ 没有找到仓库")
        return
    
    print(f"📦 使用仓库: {warehouse.name}")
    
    # 测试货物API
    print(f"\n🔍 测试API: /goods/api/goods-by-warehouse/{warehouse.id}/")
    response = client.get(f'/goods/api/goods-by-warehouse/{warehouse.id}/')
    if response.status_code == 200:
        data = response.json()
        print(f"✅ API响应正常，找到 {len(data.get('goods', []))} 个货物")
        for goods in data.get('goods', []):
            print(f"   - {goods['name']} (库存: {goods['quantity']})")
    else:
        print(f"❌ API响应失败，状态码: {response.status_code}")
    
    # 测试入库页面
    print(f"\n📥 测试入库页面")
    response = client.get('/goods/inbound/')
    if response.status_code == 200:
        print("✅ 入库页面访问正常")
    else:
        print(f"❌ 入库页面访问失败，状态码: {response.status_code}")
    
    # 测试删除功能
    goods = Goods.objects.first()
    if goods:
        print(f"\n🗑️ 测试删除功能")
        print(f"测试货物: {goods.name}")
        
        # 测试删除页面访问
        response = client.get(f'/goods/{goods.pk}/delete/')
        if response.status_code == 200:
            print("✅ 删除页面访问正常")
        else:
            print(f"❌ 删除页面访问失败，状态码: {response.status_code}")
        
        # 测试删除操作（这里不实际删除）
        print("💡 删除功能需要POST请求，请在网页界面中测试")
    else:
        print("❌ 没有货物可供测试删除")
    
    print(f"\n🌐 现在可以在浏览器中测试:")
    print(f"   入库: http://127.0.0.1:8000/goods/inbound/")
    print(f"   货物列表: http://127.0.0.1:8000/goods/list/")

if __name__ == '__main__':
    test_functionality()