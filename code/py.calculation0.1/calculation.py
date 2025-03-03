# 四则计算器


# 导入模块，取别名
import tkinter as tk  # tkinter是Python的标准GUI库。

# {实例化一个窗体对象
# 创建tkinter窗口
root = tk.Tk()  # 创建根窗口
root.title('简易计算器')  #设置标题
root.geometry('295x280+100+100')  # 设置窗口的宽高为295x280，出现的位置距离屏幕左上+100+100
root.attributes("-alpha",0.9)  # 设置半透明为90%
root.config(bg='#ffffff')  # 设置背景颜色
root.resizable(False, False)  # 设置窗口的宽高不能改变

# 定义变量
font_20 = ('宋体', 20)
font_16 = ('宋体', 16)

# 第一行
result_num = tk.StringVar()
result_num.set('')
tk.Label(root, 
         textvariable= result_num, font=font_20, height=2, width=20, justify=tk.LEFT, anchor=tk.SE, bg='#ffffff'
         ).grid(row=1, column=1, columnspan=4)

# 第二行
button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#d2d2cd')
button_back = tk.Button(root, text='<-', width=5, font=font_16, relief=tk.FLAT, bg='#d2d2cd')
button_division = tk.Button(root, text='/', width=5, font=font_16, relief=tk.FLAT, bg='#d2d2cd')
button_multiplication = tk.Button(root, text='*', width=5, font=font_16, relief=tk.FLAT, bg='#daa893')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)

# 第三行
button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_subtraction = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#daa893')
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nine.grid(row=3, column=3, padx=4, pady=2)
button_subtraction.grid(row=3, column=4, padx=4, pady=2)

# 第四行
button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#daa893')
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_addition.grid(row=4, column=4, padx=4, pady=2)

# 第五行
button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_equal = tk.Button(root, text='=', width=5, height=3, font=font_16, relief=tk.FLAT, bg='#daa893')
button_one.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_three.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

# 第六行
button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_point = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#a0a5ab')
button_zero.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
button_point.grid(row=6, column=3, padx=4, pady=2)
# }

# {点击事件
# 自定义函数
def click_button(x):
    result_num.set(result_num.get()+ x)

def calculation():
    opt_str = result_num.get()
    result = eval(opt_str)
    result_num.set(str(result))

def dele():
    result_num.set('')

def back():
    x = result_num.get()
    x = x[:-1]
    result_num.set(x)

button_addition.config(command=lambda: click_button('+'))
button_subtraction.config(command=lambda: click_button('-'))
button_multiplication.config(command=lambda: click_button('*'))
button_division.config(command=lambda: click_button('/'))
button_zero.config(command=lambda: click_button('0'))
button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_three.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_point.config(command=lambda: click_button('.'))
button_equal.config(command= calculation)
button_clear.config(command= dele)
button_back.config(command= back)
# }

# 保持窗口运行
root.mainloop()

## 打包成 单文件 
#  pyinstaller -w -F calculation.py