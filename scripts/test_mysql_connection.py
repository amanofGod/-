import os, sys, django

# 设置Django环境
sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')

print("🔗 测试MySQL数据库连接...")

try:
    django.setup()
    
    from django.db import connection
    
    print(f"数据库配置:")
    print(f"  NAME: {connection.settings_dict['NAME']}")
    print(f"  HOST: {connection.settings_dict['HOST']}")
    print(f"  PORT: {connection.settings_dict['PORT']}")
    print(f"  USER: {connection.settings_dict['USER']}")
    
    # 测试连接
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 as test")
        result = cursor.fetchone()
        
        if result and result[0] == 1:
            print("✅ MySQL数据库连接成功！")
            
            # 检查表是否存在
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"✅ 数据库中的表: {[table[0] for table in tables]}")
            
            # 尝试执行migrations
            print("\n🔄 开始数据库迁移...")
            from django.core.management import execute_from_command_line
            execute_from_command_line(['manage.py', 'makemigrations'])
            execute_from_command_line(['manage.py', 'migrate'])
            print("✅ 数据库迁移完成")
            
            # 创建超级用户
            from django.contrib.auth.models import User
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                print("✅ 管理员用户创建完成")
                print("   用户名: admin")
                print("   密码: admin123")
            else:
                print("ℹ️  管理员用户已存在")
            
        else:
            print("❌ 数据库连接测试失败")
            
except Exception as e:
    print(f"❌ 连接失败: {e}")
    print("\n请检查:")
    print("1. MySQL服务是否已启动")
    print("2. 数据库名: warehouse_management 是否存在")
    print("3. 用户名密码: root/123456 是否正确")
    print("4. 端口3306是否可访问")
    
    # 显示配置信息
    try:
        import pymysql
        print("\n尝试直接连接MySQL...")
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            port=3306,
            charset='utf8mb4'
        )
        print("✅ 直接MySQL连接成功！")
        conn.close()
    except Exception as pye:
        print(f"❌ 直接MySQL连接失败: {pye}")