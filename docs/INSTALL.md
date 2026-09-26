# 安装指南

## 系统要求

- **操作系统**: Windows 10/11, macOS, Linux
- **内存**: 至少 4GB RAM（推荐 8GB+）
- **Java**: Java 17 或更高版本
- **Python**: Python 3.8+（仅桌面应用需要）
- **网络**: 稳定的互联网连接

---

## 快速安装（推荐）

### 1. 下载
从 [Releases](https://github.com/huang9178/mc-server-website/releases) 页面下载最新版本。

### 2. 解压
将压缩包解压到任意目录。

### 3. 启动
- **网页版**: 直接用浏览器打开 `index.html`
- **桌面版**: 双击 `启动管理工具.bat`

---

## 详细安装

### 方式一：GitHub Pages（最简单）

无需安装，直接访问：
```
https://huang9178.github.io/mc-server-website/
```

### 方式二：本地网页版

1. 下载 `index.html`
2. 双击用浏览器打开
3. 在设置中配置API地址

### 方式三：桌面应用

1. 下载 `desktop-app/` 目录
2. 双击 `启动管理工具.bat`
3. 或者直接打开 `土豆服务器管理工具.html`

### 方式四：打包成exe

1. 安装 [Python](https://www.python.org/downloads/)（勾选 Add to PATH）
2. 双击 `desktop-app/build.bat`
3. 等待打包完成
4. exe文件在 `dist/` 目录

---

## 服务器部署

### 本地部署

1. 安装 Java 17
2. 下载 Fabric 服务端
3. 配置 `server.properties`
4. 启动服务器

### Oracle Cloud部署（推荐24小时运行）

详见 [Oracle部署教程](../docs/Oracle部署教程.md)

---

## 常见问题

### Q: 连接失败怎么办？
A: 检查服务器是否运行，API地址是否正确，网络是否正常。

### Q: 如何修改API地址？
A: 点右上角"⚙️ 设置"，输入新的API地址，保存即可。

### Q: 支持哪些MC版本？
A: 服务端是1.20.1，通过ViaProxy支持1.7.2到最新版本客户端。

### Q: 电脑关了还能用吗？
A: 网站能打开，但控制不了服务器（服务器在你电脑上）。需要24小时运行请部署到云服务器。
