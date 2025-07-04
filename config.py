import os
from pathlib import Path

# -----------------------------
# 项目通用配置
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

# 图表输出路径
PLOT_IMAGE_PATH = STATIC_DIR / "latest_plot.png"


# -----------------------------
# 邮件发送配置
# -----------------------------

# 如果你使用 yagmail，请先在终端执行：
# yagmail register your_email@example.com 'your_app_password'
EMAIL_SENDER = "1940669310@qq.com"          # 发件人（Yagmail已注册）
EMAIL_TO = ["tyutxf@outlook.com"]             # 收件人列表

# 邮件内容模板配置（可以也放外部 HTML 文件）
EMAIL_SUBJECT = "📰 Fear & Greed Index Daily Report"
EMAIL_BODY_TEMPLATE = """
<h2>Fear and Greed Report</h2>
<p><strong>Current Score:</strong> {score}</p>
<p><strong>Rating:</strong> {rating}</p>
<img src="cid:latest_plot.png" alt="plot" style="width:100%; max-width:800px;">
<p>Generated automatically by Daily Report Bot.</p>
"""


# -----------------------------
# 定时任务配置
# -----------------------------

SCHEDULE_HOUR = 8      # 每天发送时间（小时，24小时制）
SCHEDULE_MINUTE = 0    # 每天发送时间（分钟）


# -----------------------------
# 图表绘制配置
# -----------------------------

# 绘图尺寸
FIG_WIDTH = 16
FIG_HEIGHT = 8

# 参考线阈值
FEAR_THRESHOLD = 25
GREED_THRESHOLD = 75

# 日期刻度格式
X_AXIS_DATE_FORMAT = "%Y-%m-%d"
X_AXIS_WEEKDAY = 0   # 0 = Monday


# -----------------------------
# 其他可选配置
# -----------------------------

DEBUG = True

SECRET_KEY = "replace_with_a_random_and_secret_string"
