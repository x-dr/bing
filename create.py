import tool

def create():

    imginfo=tool.get_date()
    with open('README.md', 'w+')as fw:
        fw.write(imginfo[0]+'\n\n')
        fw.write('|      |      |      |\n')
        fw.write('| :----: | :----: | :----: |\n')
        i = 0
        for dd in tool.get_list():
            i = i+1
            fw.write('|')
            fw.write(dd)           
            if (i % 3 == 0):
                fw.write("|\n")
        if(len(tool.get_list()) % 3 != 0):
            fw.write('|')
        print(f'Create README.md Failed!')


    with open('bing-url.md', 'r+')as fi:
        content = fi.read()        
        fi.seek(0, 0)
        fi.write(imginfo[1]+'\n\n'+content)
        # fi.write(tool.get_date()[1])
        print(f'Create bing-url.md Failed!')

    with open('wallpaper.md', 'w+')as fw:
        fw.write("---"+'\n')
        fw.write("title: wallpaper"+'\n')
        fw.write("date: 2022-01-01 19:24:56"+'\n')
        fw.write("type: 'gallery'"+'\n')
        fw.write("---"+'\n\n')
        with open('README.md', 'r')as fi:
            content = fi.read()
        fw.write(content)
        print(f'Create wallpaper.md Failed!')