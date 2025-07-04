import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from datetime import datetime
from fetch_data import get_fear_greed_data

def plot_fear_greed_colored():
    data = get_fear_greed_data()
    historical = data["fear_and_greed_historical"]["data"]

    # 转换时间和得分
    dates = [datetime.fromtimestamp(item["x"] / 1000) for item in historical]
    scores = [item["y"] for item in historical]

    # 创建线段数据 [(x0,y0), (x1,y1)], ...
    segments = []
    colors = []

    for i in range(len(dates) - 1):
        x0, y0 = dates[i], scores[i]
        x1, y1 = dates[i + 1], scores[i + 1]
        segments.append([[mdates.date2num(x0), y0], [mdates.date2num(x1), y1]])

        # 判断颜色
        if y0 > 75 and y1 > 75:
            colors.append('red')
        elif y0 < 25 and y1 < 25:
            colors.append('green')
        else:
            colors.append('blue')

    # 创建分段线
    lc = LineCollection(segments, colors=colors, linewidths=2)

    # 绘图
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.add_collection(lc)
    ax.autoscale()
    # 设置横轴为每周显示一次
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1, byweekday=mdates.MO))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()


    # 添加参考线
    ax.axhline(75, color='red', linestyle='--', linewidth=1, label='Greed Threshold (75)')
    ax.axhline(25, color='green', linestyle='--', linewidth=1, label='Fear Threshold (25)')

    # 添加图例说明颜色逻辑
    legend_lines = [
        Line2D([0], [0], color='red', lw=2, label='Score > 75'),
        Line2D([0], [0], color='green', lw=2, label='Score < 25'),
        Line2D([0], [0], color='blue', lw=2, label='Neutral Zone')
    ]
    ax.legend(handles=legend_lines + ax.get_legend_handles_labels()[0], loc='upper left')



    ax.set_title("Fear and Greed Index Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.grid(True)
    ax.tick_params(axis='x', labelsize=8)  # 设置 X 轴字体大小为 8
    ax.tick_params(axis='y', labelsize=8)  # 设置 Y 轴字体大小为 8
    

    # 设置日期格式
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fear_greed_colored()
