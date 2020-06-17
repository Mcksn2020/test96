#'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'
#здесь строим график


gc0='https://chart.googleapis.com/chart?'
gc_helwor='chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World'

#gc=gc0+gc_helwor

g_cht='cht=lxy'
g_chd='chd=t:60,40|7,33'
g_chs='chs=250x100'

#g_chl='Hell|Wor'

gc=gc0+g_cht+'&'+g_chd+'&'+g_chs

#print(gc)
