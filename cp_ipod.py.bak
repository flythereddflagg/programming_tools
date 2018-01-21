import os
from shutil import copy2

rootdir = os.path.dirname("D:\\iPod_Control\\Music")
dst = "C:\\Users\\Mark Redd\\Music\\ipod"
count = 0
pcnt = 0
for root, subFolders, files in os.walk(rootdir):
    for f in files:
        if f[-4:] == ".m4a"  or\
            f[-4:] == ".mp3" or\
            f[-4:] == ".m4p"   :
            fpname = root + "\\" + f
            pcnt = count / 6750.0 * 100.0
            print "\rCopying '%s' to '%s'...    \n%d%% [%s%s]" \
                % (fpname, dst, int(pcnt),
                "#"*int(pcnt*0.8),
                "."*int(80.0 - pcnt*0.8)),
            count +=1
            copy2(fpname, dst)
            
print "\r     --- DONE --- %s\n" %(" "* 70)