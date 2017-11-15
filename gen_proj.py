import os
from sys import argv

dbg_h = r"""
/*
Zed A. Shaw's Awesome Debug Macros
Annotated by Mark Redd
*/

#ifndef __dbg_h__
#define __dbg_h__

//#define NDEBUG

#include <stdio.h>
#include <errno.h>
#include <string.h>

#ifdef NDEBUG
    #define debug(M, ...)
#else
    #define debug(M, ...) fprintf(stderr,\
        "[DEBUG] %s:%d: in_function: %s) " M "\n",\
        __FILE__, __LINE__, __FUNCTION__, ##__VA_ARGS__)
#endif

#define clean_errno() (errno == 0 ? "None" : strerror(errno))

#define log_err(M, ...) fprintf(stderr,\
    "[ERROR] (%s:%d: in_function: %s errno: %s) " M "\n",\
    __FILE__, __LINE__, __FUNCTION__, clean_errno(), ##__VA_ARGS__)

#define log_warn(M, ...) fprintf(stderr,\
    "[WARN] (%s:%d: in_function: %s errno: %s) " M "\n",\
    __FILE__, __LINE__, __FUNCTION__, clean_errno(), ##__VA_ARGS__)

#define log_info(M, ...) fprintf(stderr,\
    "[INFO] (%s:%d: in_function: %s ) " M "\n",\
    __FILE__, __LINE__, __FUNCTION__, ##__VA_ARGS__)

#define check(A, M, ...) if(!(A)) { log_err(M, ##__VA_ARGS__);\
    errno=0; goto error; }

#define sentinel(M, ...) { log_err(M, ##__VA_ARGS__);\
    errno=0; goto error; }

#define check_mem(A) check((A), "Out of memory.")

#define check_debug(A, M, ...) if(!(A)) { debug(M, ##__VA_ARGS__);\
    errno=0; goto error; }

#endif
"""

main_c = r"""
#include <stdio.h>
#include <stdlib.h>
#include "dbg.h"

int main (int argc, char* argv[])
{
    printf("Project generated successfully.")
    return 0;
}
"""

main_cpp = r"""
#include <iostream>
#include <stdlib.h>
#include "dbg.h"

using namespace std;

int main (int argc, char* argv[])
{
    cout << "Project generated successfully." << endl;
    return 0;
}
"""

makefile_c = r"""
# For windows and linux

ifeq ($(OS), Windows_NT)
	TARGETS = windows
	CLEANER = clean-windows
else
	TARGETS = linux
	CLEANER = clean-linux
endif

CC = gcc
CFLAGS = -g -Wall

SRC = main
DEBUG = dbg
OUTNAME = out

all: src/$(SRC).c  include/$(DEBUG).h
	$(CC) $(CFLAGS) -c src/$(SRC).c -o obj/$(SRC).o -I ./include
	$(CC) $(CFLAGS) obj/$(SRC).o -o $(OUTNAME).exe

.PHONY: clean-linux
clean-linux:
	rm -f obj/*.o *.exe

.PHONY: clean-windows
clean-windows:
	del obj\*.o
	del *.exe

.PHONY: clean
clean: $(CLEANER)

"""

makefile_cpp = r"""
# For windows and linux

ifeq ($(OS), Windows_NT)
	TARGETS = windows
	CLEANER = clean-windows
else
	TARGETS = linux
	CLEANER = clean-linux
endif

CC = g++
CFLAGS = -g -Wall

SRC = main
DEBUG = dbg
OUTNAME = out

all: src/$(SRC).cpp  include/$(DEBUG).h
	$(CC) $(CFLAGS) -c src/$(SRC).cpp -o obj/$(SRC).o -I ./include
	$(CC) $(CFLAGS) obj/$(SRC).o -o $(OUTNAME).exe

.PHONY: clean-linux
clean-linux:
	rm -f obj/*.o *.exe

.PHONY: clean-windows
clean-windows:
	del obj\*.o
	del *.exe

.PHONY: clean
clean: $(CLEANER)

"""

ps1 = r"""
clear
make clean
make

.\out.exe
#drmemory .\out.exe
"""

bash = r"""#!/bin/bash

set -e

make clean
clear
make

./out.exe

# valgrind ./out.exe
"""

def gen_c(proj_name, type):
    pdirs = ["", "src", "obj", "include", "docs"]
    for i in pdirs:
        os.mkdir("./%s/%s" %(proj_name, i))

    pfs = [
        [ "Makefile", makefile_c],
        [ ".gitignore", "# Excluded Files\n./obj/*.o\n./*.exe"],
        [ "README.md", "# %s" % proj_name],
        [ "test.ps1", ps1],
        [ "test.sh", bash],
        [ "src/main.c", main_c],
        [ "include/dbg.h", dbg_h],
        [ "obj/placeholder.txt", ""],
        [ "docs/placeholder.txt", ""],
        ]

    for i in pfs:
        f = open("./%s/%s" %(proj_name, i[0]), "w")
        f.write(i[1])
        f.close()


def gen_cpp(proj_name, type):
    pdirs = ["", "src", "obj", "include", "docs"]
    for i in pdirs:
        os.mkdir("./%s/%s" %(proj_name, i))

    pfs = [
        [ "Makefile", makefile_cpp],
        [ ".gitignore", "# Excluded Files\n./obj/*.o\n./*.exe"],
        [ "README.md", "# %s" % proj_name],
        [ "test.ps1", ps1],
        [ "test.sh", bash],
        [ "src/main.cpp", main_cpp],
        [ "include/dbg.h", dbg_h],
        [ "obj/placeholder.txt", ""],
        [ "docs/placeholder.txt", ""],
        ]

    for i in pfs:
        f = open("./%s/%s" %(proj_name, i[0]), "w")
        f.write(i[1])
        f.close()

def gen_py(proj_name, type):
    pass

def gen_java(proj_name, type):
    pass
        
def main():
    if len(argv) == 1:
        proj_name = raw_input("Enter proj_name name: ")
        type = raw_input("Supported Languages: (c, c++, python,"\
            " java) \nEnter primary language for project: ")
    elif len(argv) != 3:
        print "error wrong number of args"
        return
    else:
        proj_name = argv[1]
        type = argv[2]
    
    types   = ["c", "c++", "python", "java"]
    if type not in types:
        print "Type not recognized"
        return
    
    methods = [gen_c, gen_cpp, gen_py, gen_java]
    mint = types.index(type)
    methods[mint](proj_name, type)
    
    


if __name__ == '__main__':
    main()
