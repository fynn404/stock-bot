import yagmail
from core.fetch_data import get_fear_greed_data
import os

def send_email_with_plot():
    # 获取数据
    data = get_fear_greed_data()
    score = round(data["fear_and_greed_historical"]["score"], 1)
    rating = data["fear_and_greed_historical"]["rating"].title()

    # 准备 HTML 内容（图内嵌 + 动态得分）
    html = f"""
    <h2>Fear and Greed Report</h2>
    <p><strong>Current Score:</strong> {score}</p>
    <p><strong>Rating:</strong> {rating}</p>
    <img src="cid:latest_plot.png" alt="plot" style="width:100%; max-width:800px;">
    <p>Generated automatically by Daily Report Bot.</p>
    """

    # 图表路径
    image_path = "static/latest_plot.png"
    if not os.path.exists(image_path):
        print("[ERROR] latest_plot.png not found.")
        return

    # 启动 yagmail 客户端
    yag = yagmail.SMTP("your_email@example.com")

    # 发送邮件
    try:
        yag.send(
            to=["recipient1@example.com", "recipient2@example.com"],  # 收件人列表
            subject="📰 Fear & Greed Index Daily Report",
            contents=[html, image_path],  # HTML + 图片附件（会被自动内嵌）
        )
        print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

if __name__ == "__main__":
    send_email_with_plot()
