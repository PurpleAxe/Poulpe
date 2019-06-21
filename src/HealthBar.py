import pyglet


window = pyglet.window.Window(resizable = True)




batch = pyglet.graphics.Batch()

vertex_list = batch.add(2, pyglet.gl.GL_POINTS, None,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (100, 100, 100, 100, 100, 100))
    )

batch.draw()

pyglet.app.run()
