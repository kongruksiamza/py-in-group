import pyglet

path="What I've Done (Official Video).mp3"

window=pyglet.window.Window()
label=pyglet.text.Label("Play Sound",font_size=40,
                        x=window.width/2,y=window.height/2,
                        anchor_x='center',anchor_y='center')

music=pyglet.resource.media(path,streaming=False)

@window.event
def on_draw():
    window.clear()
    label.draw()
    music.play()

pyglet.app.run()
