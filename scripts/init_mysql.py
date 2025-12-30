#!/usr/bin/env python
"""
MySQL数据库初始化脚本
"""
import pymysql
import os
import sys

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'charset': 'utf8mb4'
}

def create_database():
    """创建数据库"""
    try:
        # 连接MySQL服务器（不指定数据库）
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        # 创建数据库（如果不存在）
        cursor.execute("CREATE DATABASE IF NOT EXISTS warehouse_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ 数据库 'warehouse_management' 创建成功或已存在")
        
        cursor.close()
        connection.close()
        
        return True
        
    except Exception as e:
        print(f"❌ 数据库创建失败: {e}")
        return False

def test_connection():
    """测试数据库连接"""
    try:
        # 连接到指定数据库
        config = DB_CONFIG.copy()
        config['database'] = 'warehouse_management'
        
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        
        # 测试查询
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✅ MySQL连接成功，版本: {version[0]}")
        
        cursor.close()
        connection.close()
        
        return True
        
    except Exception as e:
        print(f"❌ 数据库连接测试失败: {e}")
        return False

def main():
    print("=== MySQL数据库初始化 ===")
    print(f"主机: {DB_CONFIG['host']}")
    print(f"用户: {DB_CONFIG['user']}")
    print("正在创建数据库...")
    
    if create_database():
        if test_connection():
            print("\n🎉 数据库初始化完成！")
            print("现在可以运行Django迁移了。")
        else:
            print("\n⚠️ 数据库创建成功但连接测试失败")
    else:
        print("\n❌ 数据库初始化失败")

if __name__ == "__main__":
    main()