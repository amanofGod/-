import pymysql

print("🔗 直接测试MySQL连接...")

try:
    # 连接MySQL服务器
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        port=3306,
        charset='utf8mb4'
    )
    
    print("✅ MySQL服务器连接成功！")
    
    # 创建数据库（如果不存在）
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS warehouse_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ 数据库 warehouse_management 创建成功")
        
        # 切换到该数据库
        cursor.execute("USE warehouse_management")
        print("✅ 已切换到 warehouse_management 数据库")
        
        # 显示所有数据库
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print(f"📊 当前数据库列表: {[db[0] for db in databases if 'warehouse' in db[0] or 'information_schema' not in db[0]]}")
    
    connection.close()
    print("✅ 测试完成，MySQL配置正确！")
    
except Exception as e:
    print(f"❌ MySQL连接失败: {e}")
    print("\n请检查:")
    print("1. MySQL服务是否启动")
    print("2. 用户名密码是否正确 (root/123456)")
    print("3. 端口3306是否可用")
    print("4. 用户是否有创建数据库权限")