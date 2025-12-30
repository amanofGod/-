#!/usr/bin/env python
"""
使用MySQL数据库启动Django服务器
"""
import os
import sys
import subprocess

# 设置项目目录
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)
sys.path.insert(0, project_dir)

def check_mysql():
    """检查MySQL连接"""
    try:
        import pymysql
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': '123456',
            'database': 'warehouse_management',
            'charset': 'utf8mb4'
        }
        connection = pymysql.connect(**config)
        connection.close()
        return True
    except Exception as e:
        print(f"MySQL连接失败: {e}")
        return False

def main():
    print(f"工作目录: {os.getcwd()}")
    print("=== 使用MySQL启动Django服务器 ===")
    
    # 检查MySQL连接
    if not check_mysql():
        print("\n❌ MySQL连接失败，请检查：")
        print("1. MySQL服务是否启动")
        print("2. 数据库'warehouse_management'是否存在")
        print("3. 用户名和密码是否正确")
        print("\n请先运行 init_mysql.py 初始化数据库")
        return
    
    # 设置Django环境
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management_system.settings')
    
    try:
        import django
        django.setup()
        print("✅ Django环境设置成功")
    except Exception as e:
        print(f"❌ Django设置失败: {e}")
        return
    
    # 运行数据库迁移
    print("\n正在运行数据库迁移...")
    try:
        result = subprocess.run([sys.executable, 'manage.py', 'migrate'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 数据库迁移完成")
        else:
            print(f"❌ 数据库迁移失败: {result.stderr}")
            return
    except Exception as e:
        print(f"❌ 迁移执行失败: {e}")
        return
    
    # 显示访问地址
    print("\n=== 服务器启动信息 ===")
    print("- 首页: http://127.0.0.1:8000/")
    print("- 货物管理: http://127.0.0.1:8000/goods/list/")
    print("- 仓库管理: http://127.0.0.1:8000/warehouse/list/")
    print("- 报表分析: http://127.0.0.1:8000/reports/stock/")
    print("- 用户注册: http://127.0.0.1:8000/users/register/")
    print("\n数据库: MySQL (warehouse_management)")
    print("按Ctrl+C停止服务器")
    
    # 启动服务器
    print("\n正在启动Django开发服务器...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
    except KeyboardInterrupt:
        print("\n服务器已停止")

if __name__ == "__main__":
    main()