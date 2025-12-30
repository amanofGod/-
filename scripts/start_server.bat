@echo off
chcp 65001 >nul
echo 启动Django服务器...
cd /d "d:\good job\study\wk\ks\1\warehouse_management_system"
echo 当前目录: %CD%
echo 检查manage.py...
if exist manage.py (
    echo 找到manage.py，正在启动服务器...
    python manage.py runserver 127.0.0.1:8000
) else (
    echo 错误：找不到manage.py文件
    dir *.py
)
pause