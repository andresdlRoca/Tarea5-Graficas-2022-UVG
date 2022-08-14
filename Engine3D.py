from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend

width = 960
height = 540

rend = Renderer(width, height)

#Posiciones de camara y modelos
modelPosition1 = V3(4, 0, 0)
modelPosition2 = V3(6, 1, 0)
mediumShotPos = V3(5.3, 1, 3)
highAnglePos = V3(5, 2.6, 3)
lowAnglePos = V3(5.3, -0.5, 2.8)
dutchAnglePos = V3(5.3, 1, 2.5)


#Settings de tomas
#Para correr cada tipo de toma solo se debe de descomentar la que se vaya a utilizar y comentar las demas


# rend.glLookAt(V3(5, 0.5, 1), mediumShotPos) #Medium Shot Settings


# rend.glLookAt(V3(5, 0.5, -1), highAnglePos) #High angle shot settings


# rend.glLookAt(V3(5, 0.5, 1), lowAnglePos) # low angle shot settings


rend.glLookAt(V3(5, 0.5, 1), dutchAnglePos) # Dutch angle shot settings
rend.glViewMatrix(translate=V3(5.3, 1, 2.5), rotate=V3(0,0,-20)) # Dutch angle shot settings
rend.glProjectionMatrix(fov=80) # Dutch angle shot settings


#Renderizado de los modelos y texturas
rend.active_texture = Texture("models/seraphine.bmp")
rend.active_shader = gourad
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition1,
                scale = V3(0.5,0.5,0.5),
                rotate = V3(0,0,0))

rend.active_shader = gourad
rend.glLoadModel("models/seraphine.obj",
                translate = modelPosition2,
                scale = V3(0.4,0.4,0.4),
                rotate = V3(0,0,0))

rend.glFinish("output.bmp")

