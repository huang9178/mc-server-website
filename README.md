# 🥔 正宗土豆服务器 | 谁玩谁瞬爆

> 一个功能完整的 Minecraft 1.20.1 Fabric 服务器管理系统，支持网页控制、桌面应用、AI助手、智能手机模组等。

![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1-green)
![Fabric](https://img.shields.io/badge/Fabric-0.14.24-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## ✨ 功能特性

### 🎮 服务器功能
- ✅ Minecraft 1.20.1 Fabric 服务端
- ✅ 和平模式 + 死亡不掉落
- ✅ 高版本互通（ViaProxy，支持1.7.2到最新版本）
- ✅ 连锁挖矿模组
- ✅ 经济系统（Notches Currency）
- ✅ 智能手机模组（银行/外卖/购物/游戏/聊天/微信）
- ✅ 注册登录系统（/reg 注册，/log 登录，7天缓存）

### 🌐 网页管理面板
- ✅ 服务器推广首页
- ✅ 管理员登录（huang9178 / Hny140623）
- ✅ 实时仪表盘（CPU/内存/玩家数）
- ✅ 启动/停止/智能重启
- ✅ 实时日志 + 控制台指令
- ✅ 玩家管理（踢人/给物品）
- ✅ 数据备份与恢复
- ✅ 服务器统计

### 🤖 AI智能助手
- ✅ 健康状态分析
- ✅ 智能优化建议
- ✅ 一键优化（清理日志/检查服务）
- ✅ 状态报告生成
- ✅ 自动巡检（每30秒）
- ✅ 操作日志记录

### 🖥️ 桌面应用
- ✅ Python tkinter 桌面管理工具
- ✅ 实时状态监控
- ✅ 一键启动/停止/重启
- ✅ 实时日志查看
- ✅ 控制台指令发送
- ✅ 可自定义API地址
- ✅ 支持打包成exe

### 📱 智能手机模组
- ✅ 银行系统（余额/利息/转账）
- ✅ 外卖系统（点外卖/外卖员送餐）
- ✅ 购物商城（买任意MC物品）
- ✅ 游戏中心
- ✅ 微信式聊天（加好友/朋友圈/撤回）
- ✅ 虚拟存储系统
- ✅ 8个功能道具 + 合成配方

### 🔧 自动运维
- ✅ 智能监控（每分钟检查，崩溃自动恢复）
- ✅ 自动备份（每小时备份到GitHub）
- ✅ 开机自启（systemd / crontab）
- ✅ 内网穿透（ChmlFrp，公网访问）
- ✅ 免费域名（tudoumc.fucku.top）

---

## 🚀 快速开始

### 方式一：直接使用（推荐）

1. 打开管理面板：http://tudoumc.fucku.top:56768/
2. 管理员登录：`huang9178` / `Hny140623`
3. 启动服务器，开始玩！

### 方式二：GitHub Pages网站

1. 打开：https://huang9178.github.io/mc-server-website/
2. 点右上角"⚙️ 设置"配置API地址
3. 管理员登录后控制服务器

### 方式三：桌面应用

1. 下载 `mc-desktop-app.zip`
2. 安装Python后双击 `build.bat` 打包成exe
3. 运行 `土豆服务器管理工具.exe`

### MC连接地址
```
gz.2.frp.one:8550
```

---

## 📁 项目结构

```
mc-server/                 # MC服务器目录
├── mods/                  # 模组文件夹
├── world/                 # 世界数据
├── server.properties      # 服务器配置
└── fabric-server-launch.jar

server-panel/              # 网站管理面板
├── app.py                 # Flask后端
├── templates/             # 网页模板
├── server.db              # SQLite数据库
└── init_db.py             # 数据库初始化

smartphone-mod/            # 智能手机模组
├── src/                   # Java源码
├── build.gradle           # 构建配置
└── fabric.mod.json        # 模组配置

mc-desktop-app/            # 桌面应用
├── main.py                # 主程序
├── build.bat              # 打包脚本
└── 使用说明.txt

static-site/               # GitHub Pages静态网站
└── index.html             # 单页应用

chmlfrp/                   # 内网穿透
├── frpc                   # frpc客户端
├── frpc.ini               # MC隧道配置
└── frpc-web-sj.ini        # Web隧道配置
```

---

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| MC服务端 | Fabric 1.20.1 |
| 网站后端 | Python Flask |
| 数据库 | SQLite |
| 前端 | HTML/CSS/JavaScript |
| 桌面应用 | Python tkinter |
| 模组开发 | Java + Fabric API |
| 内网穿透 | ChmlFrp |
| 网站托管 | GitHub Pages |
| 高版本互通 | ViaProxy |

---

## 📝 命令说明

### 游戏内命令
```
/reg <密码>      # 注册账号
/log <密码>      # 登录账号
/balance         # 查看余额
/pay <玩家> <金额> # 转账
```

### 服务器管理
```bash
bash manage.sh start    # 启动所有服务
bash manage.sh stop     # 停止所有服务
bash manage.sh restart  # 重启所有服务
bash manage.sh status   # 查看状态
```

---

## ⚠️ 注意事项

1. **电脑需开机**：服务器运行在本地电脑，电脑关机则无法访问
2. **网络要求**：需要稳定的网络连接
3. **内存建议**：至少4GB内存，推荐8GB以上
4. **Java版本**：需要Java 17
5. **免费域名**：tudoumc.fucku.top 仅作演示，可自行更换

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

---

## 📄 许可证

MIT License - 可自由使用、修改、分发

---

## 🙏 致谢

- [Fabric](https://fabricmc.net/) - MC模组加载器
- [ViaProxy](https://github.com/ViaVersion/ViaProxy) - 高版本互通
- [ChmlFrp](https://www.chmlfrp.cn/) - 内网穿透
- [Notches Currency](https://modrinth.com/mod/notches-currency) - 经济模组

---

**⭐ 如果这个项目对你有帮助，点个Star支持一下吧！**
