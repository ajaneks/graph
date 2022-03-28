import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('bmh')


x_ass_koord=[1,2,3,4,5]
y_ass_koord=[10,20,30,40,50]
y_ass_koord2=[6,12,18,24,30]
y_ass_koord3=[3,6,9,12,15]


plt.xlabel("Daudzums")
plt.ylabel('Cena')
plt.title('Koka cena')
plt.plot(x_ass_koord,y_ass_koord,linewidth=3,linestyle="dotted",color="red",label="jaunais")
plt.plot(x_ass_koord,y_ass_koord2,linewidth=3,linestyle="dotted",color="green",label="gravis")
plt.bar(x_ass_koord,y_ass_koord2,label="bbno$")

plt.legend(loc="lower right")


plt.show() 
