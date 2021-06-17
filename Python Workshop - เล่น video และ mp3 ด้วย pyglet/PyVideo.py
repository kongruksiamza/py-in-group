import pyglet

path="New Divide (Official Video) - Linkin Parkwebm.mp4"


window=pyglet.window.Window(fullscreen=True)
#window=pyglet.window.Window(fullscreen=True) ภาพเต็มจอ
#window.set_size(800, 600)#กำหนดขนาด window

player=pyglet.media.Player()
source=pyglet.media.StreamingSource()
MediaLoad=pyglet.media.load(path)
player.queue(MediaLoad)
@window.event
def on_draw():
    player.play()
    if player.source and player.source.video_format:
       player.get_texture().blit(0,0)

pyglet.app.run()
