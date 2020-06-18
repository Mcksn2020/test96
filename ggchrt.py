#'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'
#здесь строим график
#все взято отсюда https://developers.google.com/chart/image/docs/gallery/line_charts

import point_calc

#x11=str(point_calc.x1)
#x12=str(point_calc.x2)
#x13=str(point_calc.x3)
x_ii=str(point_calc.x_init)
x_ee=str(point_calc.x_end)


gc='https://chart.googleapis.com/chart?'




g_cht='cht=lxy'                #линия
#g_chd='chd=t:10,20|66,99'    #точки строго в процентах
g_chd='chd=t:'+point_calc.x1+','+point_calc.x2+','+point_calc.x3
g_chd=g_chd+'|'+point_calc.y1+','+point_calc.y2+','+point_calc.y3
g_chd=g_chd+'|0,100|50,50'
#g_chs1='chs=250x100'
#g_chs2='chs=250x250'
g_chs='chs=400x400'            #   размер
g_chl='chl=ОПЦИОНЫ'                 # название
g_chc='chco=008000,000000'              # цвет линии
g_chttl='chtt=Опционный+портфель'   #название
g_chtts='chts=FF0000,20,c'         #шрифт названия
g_chxt='chxt=x,y'             #оси
g_grid='chg=20,20'              #шаг сетки
#g_chxr='chxr=0,x_ii,x_ee,str(point_calc.x_st)'  #цифры по оси Х
g_chxr='chxr=0,'+x_ii+','+x_ee+','+str(point_calc.x_st)+'|1,-1000,1000'
g_chm='chm=@V,0000FF,0,50:50,1'



gc=gc+g_cht+'&'+g_chd+'&'+g_chs+'&'+g_chc+'&'+g_chttl+'&'+g_chtts
gc=gc+'&'+g_chxt+'&'+g_grid+'&'+ g_chxr+'&'+g_chm

#print(gc)

