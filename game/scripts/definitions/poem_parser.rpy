init python:
    def parse_poem(file):
        body = ""
        with open(f"{renpy.config.gamedir}/{file}", encoding="utf-8") as f:
                    lines = f.readlines()
                    author = ""
                    title = ""
                    style = True
                    paper = None
                    music = None
                    separate_title_from_text = False
                    filename = file[file.rfind("/") + 1:file.rfind(".")]
                    properties = {}
                    if filename.endswith("s"):
                        author = "sayori"
                    elif filename.endswith("m"):
                        author = "monika"
                    elif filename.endswith("n"):
                        author = "natsuki"
                    elif filename.endswith("y"):
                        author = "yuri"
                    elif filename.endswith("t"):
                        author = "taiyen"
                    elif filename.endswith("k"):
                        author = "kotonoha"
                    while True:
                        line = lines[0].strip()
                        if not line:
                            break
                        
                        if line.startswith("# "):
                            title = line[2:].strip()
                            del lines[0]
                            continue
                    return Poem(author, title, "".join(lines).strip())