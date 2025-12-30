import os
import sys

# 设置项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)
sys.path.insert(0, project_dir)

print(f"当前目录: {os.getcwd()}")
print(f"Python路径: {sys.path[0]}")

# 检查文件
if os.path.exists('manage.py'):
    print("✅ manage.py 存在")
else:
    print("❌ manage.py 不存在")
    sys.exit(1)

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

try:
    import django
    print(f"✅ Django版本: {django.get_version()}")
    django.setup()
    print("✅ Django设置加载成功")
    
    # 测试数据库连接
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✅ 数据库连接成功")
    except Exception as e:
        print(f"❌ 数据库连接失败: {e}")
        
except Exception as e:
    print(f"❌ Django设置失败: {e}")
    import traceback
    traceback.print_exc()