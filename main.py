'''
si vous avez bien pull, ce message s'affiche.
'''

from processing import OpenData, affiche_corr, affiche_hm

print(OpenData())
affiche_corr(OpenData(), 16)
affiche_hm(OpenData())

