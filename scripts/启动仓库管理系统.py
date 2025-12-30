#!/usr/bin/env python
"""
仓库管理系统启动脚本
"""
import os
import sys
import subprocess

def main():
    print("🚀 启动仓库管理系统...")
    
    # 设置项目路径
    project_path = "d:/good job/study/wk/ks/1/warehouse_management_system"
    
    # 切换到项目目录
    os.chdir(project_path)
    print(f"📁 工作目录: {os.getcwd()}")
    
    # 检查manage.py是否存在
    if not os.path.exists('manage.py'):
        print("❌ 找不到manage.py文件")
        return
    
    # 运行数据库迁移
    print("🔄 运行数据库迁移...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True, capture_output=True)
        print("✅ 数据库迁移完成")
    except subprocess.CalledProcessError as e:
        print(f"❌ 迁移失败: {e}")
    
    # 创建管理员用户
    print("👤 创建管理员用户...")
    try:
        result = subprocess.run([sys.executable, '-c', '''
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse_management_system.settings")
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("✅ 管理员用户创建成功")
else:
    print("✅ 管理员用户已存在")
        '''], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"⚠️ 创建用户失败: {e}")
    
    print("\n" + "="*50)
    print("🎉 启动准备完成！")
    print(f"\n🌐 访问地址:")
    print(f"   http://127.0.0.1:8000/")
    print(f"   仓库管理: http://127.0.0.1:8000/warehouse/list/")
    print(f"   货物管理: http://127.0.0.1:8000/goods/list/")
    print(f"   报表分析: http://127.0.0.1:8000/reports/stock/")
    
    print(f"\n👤 登录信息:")
    print(f"   用户名: admin")
    print(f"   密码: admin123")
    
    print(f"\n🔧 现在启动Django服务器...")
    print(f"   按Ctrl+C停止服务器")
    print("="*50 + "\n")
    
    # 启动服务器
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'])
    except KeyboardInterrupt:
        print(f"\n👋 服务器已停止")

if __name__ == '__main__':
    main()