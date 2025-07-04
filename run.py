from flask import Flask, send_from_directory, render_template_string
from config import STATIC_DIR, PLOT_IMAGE_PATH

app = Flask(__name__)

# 首页：展示图表
@app.route("/")
def index():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fear and Greed Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px;
                background-color: #f8f9fa;
            }}
            img {{
                max-width: 90%;
                height: auto;
                border: 1px solid #ccc;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <h1>📊 Fear & Greed Index</h1>
        <p>Below is the latest chart generated.</p>
        <img src="/static/latest_plot.png" alt="Plot Not Found">
    </body>
    </html>
    """
    return render_template_string(html)

# 静态文件服务（Flask 默认会处理 static/，此处不一定需要）
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

# 启动服务
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
