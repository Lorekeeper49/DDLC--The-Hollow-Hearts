init python:
    import subprocess
    def switch_game(exe, *, start_data=None, blank_end_data=None):
        subprocess.run([config.gamedir + "/subgames/" + exe])