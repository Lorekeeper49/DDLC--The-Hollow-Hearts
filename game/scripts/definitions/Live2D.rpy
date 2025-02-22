init python:
    def Live2D_lipsync(self, dt):
        if renpy.music.get_playing(channel="voice"):
            self.set_parameter("ParamMouthOpenY", renpy.sound.get_volume("voice"))

define _live2d_fade = True

# image sayori anim = Live2D("Live2D/sayori", update_function=Live2D_lipsync)

# label testLive2D:
#     show sayori anim as sayo
#     $ sayo.set_param()