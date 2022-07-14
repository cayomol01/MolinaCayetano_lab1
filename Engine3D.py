#Programa para crear una ventana de Graficos que se represente a través de un mapa de bits
#El programa fue creado con la ayuda del catedrático Carlos Alonso y es casi una copia de lo hecho en clase

from gl import Renderer, color


width = 512
height = 256
rend = Renderer(width, height)


rend.glViewPort(int(width/4), int(height/4), int(width/2), int(height/2))

rend.glClearColor(0,0.5,0)
rend.glClear()

rend.glClearViewport(color(0.5,0,0))


rend.glPoint_vp(0,0)


rend.glFinish("output.bmp")
