#!/usr/bin/env python
"""
快速启动测试脚本
"""
import os
import subprocess
import sys

def quick_test():
    """快速测试页面"""
    # 启动服务器
    os.system('cd "d:/good job/study/wk/ks/1/warehouse_management_system" && python manage.py runserver --noreload')
    
if __name__ == '__main__':
    print("🚀 启动Django服务器...")
    print("访问地址: http://127.0.0.1:8000/goods/list/")
    quick_test()