import os
import sys
import subprocess
import time
import webbrowser

# 添加项目目录到Python路径
sys.path.append(r'd:\good job\study\wk\ks\1\warehouse_management_system')
os.chdir(r'd:\good job\study\wk\ks\1\warehouse_management_system')

print("=" * 60)
print("仓库管理系统 - 删除功能优化版")
print("=" * 60)

# 展示当前仓库状态
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
    import django
    django.setup()
    
    from warehouse.models import Warehouse
    
    print("\n【仓库删除状态】")
    print("-" * 30)
    warehouses = Warehouse.objects.all()
    
    for warehouse in warehouses:
        goods_count = warehouse.goods_set.count()
        if goods_count == 0:
            print(f"✅ {warehouse.name}: 可删除 (空仓库)")
        else:
            print(f"❌ {warehouse.name}: 不可删除 (有 {goods_count} 件货物)")
    
    print("\n【功能说明】")
    print("-" * 30)
    print("1. 空仓库可以直接删除")
    print("2. 有货的仓库会显示删除说明")
    print("3. 点击'删除说明'查看详细操作指南")
    
except Exception as e:
    print(f"初始化错误: {e}")

print("\n启动Django服务器...")
print("请在浏览器中查看仓库删除功能的改进效果")

# 启动服务器
try:
    server_process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', '8000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # 等待服务器启动
    time.sleep(3)
    
    # 打开浏览器到仓库列表页面
    webbrowser.open('http://127.0.0.1:8000/warehouse/list/')
    
    print("浏览器已打开到仓库列表页面")
    print("请点击任意仓库的'删除说明'查看改进效果")
    print("按Ctrl+C停止服务器")
    
    # 保持运行
    server_process.wait()
    
except KeyboardInterrupt:
    print("\n正在关闭服务器...")
    server_process.terminate()
    print("服务器已关闭")
except Exception as e:
    print(f"启动服务器失败: {e}")