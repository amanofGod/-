#!/usr/bin/env python
"""
MySQL数据库设置脚本
"""
import os
import sys

print("🔧 配置MySQL数据库连接...")

# 1. 安装mysqlclient
print("\n📦 步骤1: 安装MySQL驱动")
try:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "mysqlclient"], check=True)
    print("✅ mysqlclient安装成功")
except subprocess.CalledProcessError as e:
    print(f"❌ mysqlclient安装失败: {e}")
    print("请手动运行: pip install mysqlclient")
    sys.exit(1)

# 2. 创建MySQL数据库
print("\n🗄️ 步骤2: 创建MySQL数据库")
print("请确保MySQL服务已启动，然后执行以下SQL命令:")
print("CREATE DATABASE IF NOT EXISTS warehouse_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
print("（如果你已有该数据库，可以跳过此步骤）")

# 3. 测试数据库连接
print("\n🔗 步骤3: 测试数据库连接")
try:
    sys.path.insert(0, 'd:/good job/study/wk/ks/1/warehouse_management_system')
    os.chdir('d:/good job/study/wk/ks/1/warehouse_management_system')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
    
    import django
    django.setup()
    
    from django.db import connection
    from django.core.management import call_command
    
    # 测试连接
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result:
            print("✅ MySQL数据库连接成功！")
    
    # 迁移数据库表
    print("\n🔄 步骤4: 创建数据库表")
    call_command('makemigrations')
    call_command('migrate')
    print("✅ 数据库表创建完成")
    
    # 创建超级用户
    print("\n👤 步骤5: 创建管理员用户")
    from django.contrib.auth.models import User
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("✅ 管理员用户创建成功")
        print("   用户名: admin")
        print("   密码: admin123")
    else:
        print("ℹ️  管理员用户已存在")
    
    print("\n🎉 MySQL数据库配置完成！")
    print("现在可以启动服务器: python start_django.py")
    
except Exception as e:
    print(f"❌ 数据库连接失败: {e}")
    print("\n请检查:")
    print("1. MySQL服务是否启动")
    print("2. 用户名密码是否正确 (root/123456)")
    print("3. 数据库warehouse_management是否存在")
    print("4. 用户是否有数据库操作权限")