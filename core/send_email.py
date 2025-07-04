import yagmail
from core.fetch_data import get_fear_greed_data
import os
from config import EMAIL_SENDER, EMAIL_TO, EMAIL_SUBJECT, EMAIL_BODY_TEMPLATE, PLOT_IMAGE_PATH

def send_email_with_plot():
    # 获取数据
    data = get_fear_greed_data()
    score = round(data["fear_and_greed_historical"]["score"], 1)
    rating = data["fear_and_greed_historical"]["rating"].title()

    # 邮件内容
    html = EMAIL_BODY_TEMPLATE.format(score=score, rating=rating)

    # 图表路径
    image_path = str(PLOT_IMAGE_PATH)
    if not os.path.exists(image_path):
        print("[ERROR] latest_plot.png not found.")
        return

    # 启动 yagmail 客户端
    yag = yagmail.SMTP(EMAIL_SENDER)

    # 发送邮件
    try:
        yag.send(
            to=EMAIL_TO,
            subject=EMAIL_SUBJECT,
            contents=[html, image_path],
        )
        print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

if __name__ == "__main__":
    send_email_with_plot()
