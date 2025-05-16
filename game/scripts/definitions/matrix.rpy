screen matrixeffect(width, *, chars, fonts, space=0, lengths=None, sizes=None, colors=["#0f08"], timers=None, vert=True):
    if vert:
        hbox:
            spacing space

            $ strings = [""] * width
            for i in range(width):
                text strings[i] font fonts[i % len(fonts)] size sizes[i % len(sizes)] color colors[i % len(colors)] vertical True