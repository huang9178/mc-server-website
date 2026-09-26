<div align="center">

# 🥔 正宗土豆服务器

### 谁玩谁瞬爆 | Minecraft 1.20.1 Fabric 服务器管理系统

[![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1-62B47A?style=for-the-badge)](https://www.minecraft.net/)
[![Fabric](https://img.shields.io/badge/Fabric-0.14.24-DBD0B5?style=for-the-badge)](https://fabricmc.net/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/huang9178/mc-server-website?style=for-the-badge)](https://github.com/huang9178/mc-server-website/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/huang9178/mc-server-website?style=for-the-badge)](https://github.com/huang9178/mc-server-website/network/members)

**一个功能完整的 Minecraft 服务器管理系统，支持网页控制、桌面应用、AI助手、智能手机模组**

[在线演示](https://huang9178.github.io/mc-server-website/) · [文档](docs/) · [报告Bug](https://github.com/huang9178/mc-server-website/issues) · [功能建议](https://github.com/huang9178/mc-server-website/issues)

</div>

---

## 📋 目录

- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [项目结构](#-项目结构)
- [安装指南](#-安装指南)
- [使用说明](#-使用说明)
- [技术栈](#-技术栈)
- [贡献指南](#-贡献指南)
- [许可证](#-许可证)

---

## ✨ 功能特性

### 🎮 服务器核心
- **Minecraft 1.20.1 Fabric** 服务端
- **和平模式** + **死亡不掉落**
- **高版本互通** - ViaProxy 支持 1.7.2 到最新版本
- **连锁挖矿** - 一键挖矿
- **经济系统** - Notches Currency
- **注册登录** - /reg 注册，/log 登录，7天缓存

### 🌐 网页管理面板
- **推广首页** - 服务器介绍
- **管理员登录** - 安全认证
- **实时仪表盘** - CPU/内存/玩家数监控
- **一键控制** - 启动/停止/智能重启
- **玩家管理** - 踢人/给物品
- **数据备份** - 自动+手动备份
- **实时日志** - 控制台指令

### 🤖 AI智能助手
- **健康分析** - 自动检测服务器状态
- **智能建议** - 优化建议
- **一键优化** - 清理日志/检查服务
- **状态报告** - 完整报告生成
- **自动巡检** - 每30秒分析
- **操作日志** - 记录所有操作

### 🖥️ 桌面应用
- **跨平台** - Windows/macOS/Linux
- **实时监控** - 状态实时更新
- **一键控制** - 启动/停止/重启
- **日志查看** - 实时日志
- **指令发送** - 控制台指令
- **可打包exe** - PyInstaller打包

### 📱 智能手机模组
- **银行系统** - 余额/利息/转账
- **外卖系统** - 点外卖/外卖员送餐
- **购物商城** - 购买任意MC物品
- **游戏中心** - 小游戏
- **微信聊天** - 加好友/朋友圈/撤回
- **虚拟存储** - 物品存储
- **8个道具** - 合成配方

### 🔧 自动运维
- **智能监控** - 每分钟检查，崩溃自动恢复
- **自动备份** - 每小时备份到GitHub
- **开机自启** - systemd/crontab
- **内网穿透** - ChmlFrp 公网访问
- **免费域名** - 自定义域名

---

## 🚀 快速开始

### 方式一：在线使用（推荐）

👉 **[点击打开管理面板](http://tudoumc.fucku.top:56768/)**

管理员账号：`huang9178` / 密码：`Hny140623`

### 方式二：GitHub Pages

🌐 **https://huang9178.github.io/mc-server-website/**

### 方式三：桌面应用

1. 下载 [desktop-app.zip](https://github.com/huang9178/mc-server-website/archive/refs/heads/main.zip)
2. 解压，双击 `启动管理工具.bat`
3. 开始使用！

### MC连接地址
```
gz.2.frp.one:8550
```

---

## 📁 项目结构

```
mc-server-website/
├── index.html              # 网页管理面板（GitHub Pages）
├── README.md               # 项目说明
├── LICENSE                 # MIT许可证
├── CONTRIBUTING.md         # 贡献指南
├── desktop-app/            # 桌面应用
│   ├── 土豆服务器管理工具.html  # HTML版桌面应用
│   ├── 启动管理工具.bat        # 一键启动
│   ├── main.py             # Python版桌面应用
│   ├── build.bat           # 打包exe脚本
│   └── README.txt          # 使用说明
├── docs/                   # 文档
│   ├── INSTALL.md          # 安装指南
│   └── USAGE.md            # 使用指南
├── screenshots/            # 截图
└── .github/                # GitHub配置
```

---

## 📦 安装指南

详见 [安装指南](docs/INSTALL.md)

### 系统要求
- **内存**: 4GB+（推荐8GB）
- **Java**: 17+
- **Python**: 3.8+（桌面应用）
- **网络**: 稳定连接

### 快速安装
```bash
# 克隆仓库
git clone https://github.com/huang9178/mc-server-website.git
cd mc-server-website

# 网页版：直接打开 index.html

# 桌面版
cd desktop-app
python main.py
```

---

## 📖 使用说明

详见 [使用指南](docs/USAGE.md)

### 游戏内命令
```
/reg <密码>          # 注册
/log <密码>          # 登录
/balance             # 查看余额
/pay <玩家> <金额>   # 转账
```

### 管理命令
```bash
bash manage.sh start    # 启动
bash manage.sh stop     # 停止
bash manage.sh restart  # 重启
bash manage.sh status   # 状态
```

---

## 🛠️ 技术栈

| 组件 | 技术 | 版本 |
|------|------|------|
| MC服务端 | Fabric | 1.20.1 |
| 网站后端 | Python Flask | 2.0+ |
| 数据库 | SQLite | 3.0+ |
| 前端 | HTML/CSS/JS | ES6+ |
| 桌面应用 | Python tkinter | 3.8+ |
| 模组开发 | Java + Fabric API | 17 |
| 内网穿透 | ChmlFrp | - |
| 网站托管 | GitHub Pages | - |
| 高版本互通 | ViaProxy | 3.4.12 |

---

## 🤝 贡献指南

我们欢迎任何形式的贡献！详见 [贡献指南](CONTRIBUTING.md)

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

---

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源，可自由使用、修改、分发。

---

## 🙏 致谢

- [Fabric](https://fabricmc.net/) - MC模组加载器
- [ViaProxy](https://github.com/ViaVersion/ViaProxy) - 高版本互通
- [ChmlFrp](https://www.chmlfrp.cn/) - 内网穿透
- [Notches Currency](https://modrinth.com/mod/notches-currency) - 经济模组

---

<div align="center">

**⭐ 如果这个项目对你有帮助，点个 Star 支持一下吧！**

Made with ❤️ by 正宗土豆服务器团队

</div>
