# 齿轮计算程序

# 导入模块，取别名
import tkinter as tk  # tkinter是Python的标准GUI库。
from  tkinter import ttk

# {实例化一个窗体对象
# 创建tkinter窗口
root = tk.Tk()  # 创建根窗口
root.title('渐开线圆柱齿轮计算 v0.01')  # 设置窗口的标题
root.iconbitmap(bitmap=None) # 设置窗口的图标，需指定图标文件(*.ico)的位置
root.geometry('650x500+100+100')  # 设置窗口的宽高为295x280，出现的位置距离屏幕左上+100+100
root.resizable(False, False)  # 设置窗口的宽高不能改变
root.attributes("-alpha", 1)  # 设置半透明为100%
root.config(bg='#ffffff')  # 设置背景颜色


# 基础参数输入
jiChuCanShu = tk.LabelFrame(root, text='基础参数输入', padx=5, pady=5)
jiChuCanShu.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

tk.Label(jiChuCanShu, text='齿轮类型').grid(row=0, column=0)
chiLunType = ttk.Combobox(jiChuCanShu)
chiLunType['values'] = ['外啮合', '内啮合']
chiLunType.current(0)
chiLunType.grid(row=0, column=1)

tk.Label(jiChuCanShu, text='齿轮1').grid(row=1, column=1)
tk.Label(jiChuCanShu, text='齿轮2').grid(row=1, column=2)

tk.Label(jiChuCanShu, text='法向模数m_n(mm):').grid(row=2, column=0)
tk.Entry(jiChuCanShu).grid(row=2, column=1, columnspan=2)

tk.Label(jiChuCanShu, text='法向压力角alpha_n(°):').grid(row=3, column=0)
tk.Entry(jiChuCanShu).grid(row=3, column=1, columnspan=2)

tk.Label(jiChuCanShu, text='螺旋角beta(°):').grid(row=4, column=0)
tk.Entry(jiChuCanShu).grid(row=4, column=1, columnspan=2)

tk.Label(jiChuCanShu, text='齿数z:').grid(row=5, column=0)
tk.Entry(jiChuCanShu).grid(row=5, column=1)
tk.Entry(jiChuCanShu).grid(row=5, column=2)









# 保持窗口运行
root.mainloop()