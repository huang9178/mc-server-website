# 贡献指南

感谢你对正宗土豆服务器项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 1. 报告 Bug
- 在 [Issues](https://github.com/huang9178/mc-server-website/issues) 页面提交
- 详细描述问题复现步骤
- 附上截图和错误日志

### 2. 提交功能建议
- 在 Issues 中使用 "enhancement" 标签
- 描述功能需求和使用场景

### 3. 提交代码
1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/你的功能`
3. 提交更改：`git commit -m '添加xxx功能'`
4. 推送到分支：`git push origin feature/你的功能`
5. 创建 Pull Request

## 代码规范

### Python
- 遵循 PEP 8 规范
- 使用 4 空格缩进
- 函数和变量使用 snake_case
- 添加必要的注释

### JavaScript
- 使用 ES6+ 语法
- 使用 2 空格缩进
- 变量使用 camelCase
- 避免全局变量污染

### HTML/CSS
- 使用语义化标签
- CSS 使用类选择器
- 响应式设计

### Java（模组）
- 遵循 Oracle 代码规范
- 使用 4 空格缩进
- 类名使用 PascalCase

## 提交信息规范

```
<类型>: <简短描述>

类型：
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 格式调整
- refactor: 重构
- test: 测试相关
- chore: 构建/工具相关
```

示例：
```
feat: 添加AI智能助手功能
fix: 修复服务器状态刷新问题
docs: 更新安装指南
```

## 开发环境搭建

### 前置要求
- Python 3.8+
- Node.js 14+（可选）
- Java 17（模组开发）
- Git

### 本地开发
```bash
# 克隆仓库
git clone https://github.com/huang9178/mc-server-website.git
cd mc-server-website

# 运行网页版
# 直接用浏览器打开 index.html

# 运行桌面版
cd desktop-app
python main.py

# 运行服务器后端
cd server-panel
pip install flask psutil
python app.py
```

## 测试

提交代码前请确保：
- 代码能正常运行
- 没有语法错误
- 基本功能测试通过

## 行为准则

- 尊重他人，友善交流
- 接受建设性批评
- 关注项目目标
- 帮助新手

## 联系方式

- GitHub Issues: https://github.com/huang9178/mc-server-website/issues
- 邮箱: 19127574815@163.com

再次感谢你的贡献！🎉
