#'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'
#здесь строим график


gc0='https://chart.googleapis.com/chart?'
gc_helwor='chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'

#gc=gc0+gc_helwor

g_cht='cht=lxy'                #линия
g_chd='chd=t:10.5,40|7,33'    #точки
#g_chs1='chs=250x100'
#g_chs2='chs=250x250'
g_chs='chs=300x300'            #   размер
g_chl='chl=ОПЦИОНЫ'                 # название
g_chc='chco=00FF00'              # цвет линии

gc=gc0+g_cht+'&'+g_chd+'&'+g_chs+'&'+g_chl+'&'+g_chc

#print(gc)

