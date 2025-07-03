# Daily Report App

这是一个用 Python 和 Flask 构建的每日数据抓取与图表生成的自动化项目，支持定时获取数据，绘制图表，并通过邮件发送报告。

## 功能

* 每天自动抓取数据（示例用 CNN Fear and Greed 指数）
* 生成折线图表保存为图片
* 通过 SMTP 邮件发送带图表的报告
* 可选的 Flask Web 界面展示最新图表
* 任务调度支持（APScheduler 或系统 cron）

## 项目结构

```
daily_report_app/
├── app/                   # Flask Web 应用代码
├── core/                  # 核心业务模块（数据抓取、绘图、邮件）
├── static/                # 静态资源，图表图片等
├── config.py              # 配置文件（API、邮件等）
├── run.py                 # 启动脚本
├── requirements.txt       # 依赖列表
└── README.md              # 项目说明
```

## 环境准备

建议使用虚拟环境，避免影响系统 Python。

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 配置

编辑 `config.py`，填写你的邮箱 SMTP 服务器、账户和密码等配置。

示例：

```python
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USER = 'your_email@example.com'
EMAIL_PASS = 'your_password'
```

## 运行

* 启动 Flask Web 服务：

```bash
python run.py
```

* 手动运行数据抓取和绘图：

```bash
python core/fetch_data.py
python core/generate_plot.py
python core/send_email.py
```

* 设置定时任务（示例用 APScheduler）：

```bash
python core/scheduler.py
```

## 依赖

* Flask
* requests
* matplotlib
* APScheduler
* pandas (可选)

## 贡献

欢迎提 Issue 或 Pull Request。

## 许可证

MIT License