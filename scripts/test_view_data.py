#!/usr/bin/env python
import os
import sys
import django

# 添加项目路径
sys.path.append('d:/good job/study/wk/ks/1/warehouse_management_system')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth import get_user_model
from goods.views import goods_list_view

User = get_user_model()

# 创建或获取测试用户
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com', 'password': 'testpass123'}
)

# 创建模拟请求
factory = RequestFactory()
request = factory.get('/goods/')
request.user = user

# 调用视图
try:
    # 跳过登录装饰器进行测试
    from goods.views import goods_list_view
    from django.contrib.auth.decorators import login_required
    
    # 直接调用视图函数（绕过装饰器）
    def view_without_login(request):
        # 直接执行视图逻辑
        from goods.models import Goods
        from goods.forms import GoodsSearchForm
        from django.db.models import Sum
        
        form = GoodsSearchForm(request.GET)
        goods_list = Goods.objects.select_related('warehouse').all()
        
        # 搜索功能
        if form.is_valid() and form.cleaned_data.get('search_term'):
            search_term = form.cleaned_data['search_term']
            goods_list = goods_list.filter(name__icontains=search_term)
        
        # 统计数据
        total_goods = goods_list.count()
        total_quantity = goods_list.aggregate(total=Sum('quantity'))['total'] or 0
        low_stock_count = goods_list.filter(quantity__lte=10).count()
        normal_stock_count = goods_list.filter(quantity__gt=50).count()
        
        # 模拟库存总值（单价随机生成，实际应用中应该有价格字段）
        total_value = total_quantity * 150  # 假设平均单价150元
        
        return {
            'goods_list': goods_list,
            'form': form,
            'stats': {
                'total_goods': total_goods,
                'total_quantity': total_quantity,
                'low_stock_count': low_stock_count,
                'normal_stock_count': normal_stock_count,
                'total_value': total_value
            }
        }
    
    context = view_without_login(request)
    
    print("=== 模板上下文数据 ===")
    
    if 'stats' in context:
        stats = context['stats']
        print(f"货物种类: {stats.get('total_goods', 'N/A')}")
        print(f"总库存量: {stats.get('total_quantity', 'N/A')}")
        print(f"库存预警: {stats.get('low_stock_count', 'N/A')}")
        print(f"库存正常: {stats.get('normal_stock_count', 'N/A')}")
        print(f"库存总值: {stats.get('total_value', 'N/A')}")
    
    if 'goods_list' in context:
        goods_list = context['goods_list']
        print(f"\n货物列表数量: {goods_list.count()}")
        print("货物详情:")
        for goods in goods_list:
            print(f"  - {goods.name}: {goods.quantity}件")
        
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()