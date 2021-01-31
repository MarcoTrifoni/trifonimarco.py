Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import  matplotlib  as  mpl
import  numpy  as np
import  matplotlib . pyplot  as plt
#guizero
from guizero import app
app = (title="grafico")
app.display ()

# definisco le x della curva
x  =  np . linspace ( 0 , 30 , 500 )

# definisco le y della curva
y  =  np . sin ( x ) *  np . exp ( - x / 10 )

fig , assi  =  plt.sottotrame ( 1 , 3 , figsize = ( 9 , 3 ), subplot_kw = { 'facecolor' : "# ebf5ff" })

assi [ 0 ]. grafico ( x , y , lw = 2 )
assi [ 0 ]. set_xlim ( - 5 , 35 )
assi [ 0 ]. set_ylim ( - 1 , 1 )
assi [ 0 ]. set_title ( "valori definiti" )

assi [ 1 ]. grafico ( x , y , lw = 2 )
assi [ 1 ]. asse ( 'tight' )
assi [ 1 ]. set_title ( "axis ('tight')" )

assi [ 2 ]. grafico ( x , y , lw = 2 )
assi [ 2 ]. asse ( "equal" )
assi [ 2 ]. set_title ( "axis ('equal')" )

plt.mostra ()