@echo off
chcp 65001 >nul
echo ========================================
echo   正宗土豆服务器 - 桌面应用打包工具
echo ========================================
echo.

echo [1/3] 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到Python，请先安装Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [2/3] 安装依赖...
pip install requests pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

echo [3/3] 打包成exe...
pyinstaller --onefile --windowed --name "土豆服务器管理工具" --icon=NONE main.py

echo.
echo ========================================
echo   打包完成！
echo ========================================
echo.
echo exe文件位置: dist\土豆服务器管理工具.exe
echo.
echo 双击即可运行，无需安装Python
echo.
pause
