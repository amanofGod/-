import os, sys, subprocess, time, webbrowser

# 启动Django服务器
project_dir = r'd:\good job\study\wk\ks\1\warehouse_management_system'
os.chdir(project_dir)

print("正在启动Django服务器...")
print("请访问: http://127.0.0.1:8000/reports/stock/")
print("测试库存报表的仓库筛选功能")
print("请打开浏览器开发者工具查看控制台输出")
print("\n按Ctrl+C停止服务器")

# 启动服务器
proc = subprocess.Popen([sys.executable, 'manage.py', 'runserver', '8000'], 
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 等待一下让服务器启动
time.sleep(3)

# 打开浏览器
webbrowser.open('http://127.0.0.1:8000/reports/stock/')

try:
    while True:
        line = proc.stderr.readline()
        if line:
            print(line.strip())
        elif proc.poll() is not None:
            break
except KeyboardInterrupt:
    print("\n正在停止服务器...")
    proc.terminate()
    proc.wait()

print("服务器已停止")