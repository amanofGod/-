#!/usr/bin/env python
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 检查报表模板和视图...")

# 检查模板文件是否存在
template_files = [
    'templates/reports/stock_report.html',
    'templates/reports/inbound_report.html', 
    'templates/reports/outbound_report.html',
    'templates/reports/warehouse_report.html',
    'templates/reports/inbound_outbound_report.html'
]

for template in template_files:
    if os.path.exists(template):
        print(f"✅ {template} 存在")
    else:
        print(f"❌ {template} 不存在")

# 测试报表视图导入
try:
    from reports.views import (
        stock_report_view,
        warehouse_report_view,
        inbound_report_view,
        outbound_report_view,
        inbound_outbound_report_view
    )
    print("✅ 所有报表视图导入成功")
except Exception as e:
    print(f"❌ 报表视图导入失败: {e}")

# 检查数据模型
try:
    from django.contrib.auth.models import User
    from warehouse.models import Warehouse
    from goods.models import Goods, InboundRecord, OutboundRecord
    
    print(f"✅ 用户模型正常，共 {User.objects.count()} 个用户")
    print(f"✅ 仓库模型正常，共 {Warehouse.objects.count()} 个仓库")
    print(f"✅ 货物模型正常，共 {Goods.objects.count()} 个货物")
    print(f"✅ 入库记录模型正常，共 {InboundRecord.objects.count()} 条记录")
    print(f"✅ 出库记录模型正常，共 {OutboundRecord.objects.count()} 条记录")
    
except Exception as e:
    print(f"❌ 数据模型检查失败: {e}")

print("\n🎉 报表系统检查完成！")
print("现在可以启动服务器测试报表功能:")
print("python run_server.py")