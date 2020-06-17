#'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'
#здесь строим график
#все взято отсюда https://developers.google.com/chart/image/docs/gallery/line_charts

gc0='https://chart.googleapis.com/chart?'
gc_helwor='chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'

#gc=gc0+gc_helwor

g_cht='cht=lxy'                #линия
g_chd='chd=t:10.5,40|7,33'    #точки
#g_chs1='chs=250x100'
#g_chs2='chs=250x250'
g_chs='chs=400x400'            #   размер
g_chl='chl=ОПЦИОНЫ'                 # название
g_chc='chco=00FF00'              # цвет линии
g_chttl='chtt=Опционный+портфель'   #название
g_chtts='chts=FF0000,20,c'         #шрифт названия
g_chxt='chxt=x,y,r,t'
g_grid='chg=10,20'

gc=gc0+g_cht+'&'+g_chd+'&'+g_chs+'&'+g_chc+'&'+g_chttl+'&'+g_chtts
gc=gc+'&'+g_chxt+'&'+g_grid

#print(gc)

