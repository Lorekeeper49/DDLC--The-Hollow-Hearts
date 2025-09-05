init python:
    def parse_poem(file):
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
    
    def parse_intro(file):
        with open(f"{renpy.config.gamedir}/{file}", encoding="utf-8") as f:
            lines = f.readlines()
            kan = ""
            name = ""
            attr = ""
            img = ""
            while True:
                line = lines[0].strip()
                if not line:
                    break
                if line.startswith("# "):
                    kan = line[2:].strip()
                    del lines[0]
                    continue
                if line.startswith("$ "):
                    name = line[2:].strip()
                    del lines[0]
                    continue
                if line.startswith("- "):
                    attr += line.strip() + "\n"
                    del lines[0]
                    continue
                if line.startswith("! "):
                    img = line[2:].strip()
                    del lines[0]
                    continue
            return Intro(kan, name, attr, "".join(lines).strip(), img)