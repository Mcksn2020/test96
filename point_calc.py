#готовим точки для графика

x_m=2000      #по оси Х будет этот диапазон стоимость фьючерса и он изменяется пользователем
y_m=2000      #по оси У будет этот диапазон прибыли/убытка
#соотношение между масштабами х и у  пока не понятно

f_curr=69500   # текущее значение фьючерса из файла quick

#для chxr:
x_init=f_curr-x_m/2
x_end=f_curr+x_m/2
x_st=x_m/5


op_str=69000   #страйк рассматриваемого опциона, сообщает пользователь
op_prc=800     #стоимость приобретения опциона, сообщает пользователь

#точки по оси Х:
x1=x_init
x2=op_str
x3=x_end
# 1- будет гораздо больше точек  2- проверка на диапазон  3-организовать массив

#точки по оси У
#y1=op_prc, y2=op_prc, y3=x3-op_str




