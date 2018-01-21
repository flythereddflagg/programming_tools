import os
import eyed3

#rootdir = os.path.dirname("M:\\ziTunes\\marks_ipod_bak")
#rootdir = os.path.dirname(".")


for root, subFolders, files in os.walk("."):
    for f in files:
        if f[-4:] == ".mp3":
            audiofile = eyed3.load(f)
            print("found", audiofile.tag.title)
            new_name = audiofile.tag.artist + "\\" +\
                audiofile.tag.album + "\\" +\
                audiofile.tag.title + f[-4:]
            print("renaming %s to %s"%(f, new_name))
            os.renames(root + "\\" + f, root + "\\" + new_name)
    break