# 游戏数据库备份

本目录包含正宗土豆服务器的完整数据库和配置文件备份。

## 📁 目录结构

```
data/
├── database/
│   └── server.db              # 网站管理面板数据库（SQLite，11张表）
├── server-config/
│   ├── server.properties      # MC服务器配置
│   ├── ops.json               # 管理员列表
│   ├── whitelist.json         # 白名单
│   ├── banned-players.json    # 封禁玩家
│   ├── banned-ips.json        # 封禁IP
│   └── mod-config/            # 所有模组配置文件
└── world-backup.zip           # 游戏世界完整备份（19M压缩后12M）
```

## 📊 数据库说明

### server.db（网站管理面板）
SQLite数据库，包含11张表：
- players - 玩家信息
- economy - 经济系统
- backups - 备份记录
- logs - 操作日志
- settings - 系统设置
- 等等...

### 世界数据
包含完整的游戏世界：
- 玩家建筑和进度
- 经济数据
- 领地数据
- 模组数据

## 🔄 恢复方法

### 恢复网站数据库
```bash
cp data/database/server.db server-panel/server.db
```

### 恢复服务器配置
```bash
cp data/server-config/server.properties mc-server/
cp data/server-config/ops.json mc-server/
cp -r data/server-config/mod-config/* mc-server/config/
```

### 恢复世界数据
```bash
cd mc-server
unzip ../data/world-backup.zip
```

## ⚠️ 注意

- 数据库包含玩家隐私信息，请勿公开分享
- 世界数据较大，克隆仓库时可能需要较长时间
- 建议定期更新备份
- 恢复前请先停止服务器
