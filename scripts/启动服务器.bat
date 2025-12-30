@echo off
chcp 65001 >nul
echo 🚀 启动仓库管理系统
echo ========================================
echo 🌐 访问地址: http://127.0.0.1:8000/
echo 👤 管理员账号: admin / admin123
echo 🛑 按Ctrl+C停止服务器
echo ========================================
cd /d "d:/good job/study/wk/ks/1/warehouse_management_system"
python manage.py runserver 127.0.0.1:8000
pause