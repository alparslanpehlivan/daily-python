# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:38:21 2019
"""

# Çizgi Grafiği
# color = renk, label = etiket, linewidth = çizgi genişliği, alpha = opaklık, grid = ızgara, linestyle = çizgi stili

veri.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
veri.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')

plt.legend(loc='upper right')     # legend = etiketi grafiğe koyar
plt.xlabel('x ekseni')              # label = etiket adı
plt.ylabel('y ekseni')
plt.title('Grafiğin Başlığı')            # title = grafiğin başlığı

plt.show()
