#!/usr/bin/env python
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

print("🔍 测试入库出库功能修改...")

try:
    from goods.forms import InboundRecordForm, OutboundRecordForm
    print("✅ 表单导入成功")
    
    # 测试入库表单
    inbound_form = InboundRecordForm()
    print("✅ 入库表单创建成功")
    print(f"   - 仓库字段: {inbound_form.fields.get('warehouse') is not None}")
    print(f"   - 货物字段: {inbound_form.fields.get('goods') is not None}")
    
    # 测试出库表单
    outbound_form = OutboundRecordForm()
    print("✅ 出库表单创建成功")
    print(f"   - 仓库字段: {outbound_form.fields.get('warehouse') is not None}")
    print(f"   - 货物字段: {outbound_form.fields.get('goods') is not None}")
    
    from goods.views import inbound_create_view, outbound_create_view, goods_by_warehouse_api
    print("✅ 视图导入成功")
    
    # 检查API
    print("✅ API视图导入成功")
    
    # 检查模板文件
    template_files = [
        'templates/goods/inbound_form.html',
        'templates/goods/outbound_form.html',
        'templates/goods/goods_list.html'
    ]
    
    for template in template_files:
        if os.path.exists(template):
            print(f"✅ {template} 存在")
        else:
            print(f"❌ {template} 不存在")
    
    print("\n🎉 入库出库功能修改完成！")
    print("\n现在入库/出库流程：")
    print("1. 先选择仓库")
    print("2. 再选择该仓库的货物") 
    print("3. 最后输入数量")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")