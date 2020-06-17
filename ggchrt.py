#'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'
#здесь строим график


gc0='https://chart.googleapis.com/chart?'
gc_helwor='chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'

#gc=gc0+gc_helwor

g_cht='cht=lxy'
g_chd='chd=t:10.5,40|7,33'
g_chs1='chs=250x100'
g_chs2='chs=250x250'
g_chs3='chs=300x300'
g_chl='ОПЦИОНЫ'

#gc=gc0+g_cht+'&'+g_chd+'&'+g_chs

gc1=gc0+g_cht+'&'+g_chd+'&'+g_chs1+'&'+g_chl
gc2=gc0+g_cht+'&'+g_chd+'&'+g_chs2+'&'+g_chl
gc3=gc0+g_cht+'&'+g_chd+'&'+g_chs3+'&'+g_chl

#print(gc)
