from flask import Blueprint, render_template, redirect, url_for, flash
from core.generate_plot import plot_fear_greed_colored

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def index():
    # 首页渲染前自动生成一次图表，确保图片存在
    plot_fear_greed_colored()
    return render_template("index.html")

@main_blueprint.route("/refresh")
def refresh():
    try:
        # 重新抓取数据并生成图表
        plot_fear_greed_colored()
        flash('Chart refreshed successfully.', 'success')
    except Exception as e:
        flash(f'Failed to refresh chart: {e}', 'danger')
    # 刷新后重定向回首页
    return redirect(url_for('main.index'))