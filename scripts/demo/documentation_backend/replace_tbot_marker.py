#!/usr/bin/python
#
# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# search the input file for "tbot_ref:" markers
# and search for the filename in the tcpath
# replace the marker with the content of the
# filename it refers. Write the new file to
# the outputfile
# 
import os, sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--inputfile",
       dest="ifile", default="none",
       help="input file")
parser.add_option("-o", "--outputfile",
       dest="ofile", default="none",
       help="output file")
parser.add_option("-t", "--tcpatch",
       dest="tcpath", default="none",
       help="path to logfiles.")
(options, args) = parser.parse_args()
 
searchstring = 'tbot_ref:'

fi = open(options.ifile, 'r')
fo = open(options.ofile, 'w')
line = fi.readline()

while line:
    found = line.find(searchstring)
    if found != -1:
        fo.write("\n::\n\n")
        # get filename
        logfile = line.split(searchstring)
        logfile = logfile[1]
        logfile = logfile.replace('\n', '')
        # open filename
        fl = open(options.tcpath + logfile, 'r')
        if not fl:
            print("Error: %s not found\n" %(options.tcpath + logfile))
            sys.exit(1)
        # write line by line + 2 ' ' before the original line
        ln = fl.readline()
        while ln:
            ln = ln.replace('\r\n','\n')
            ln = ln.replace('\r','\n  ')
            fo.write('  ' + ln)
            ln = fl.readline()

        fo.write("\n")
        fl.close()
    else:
        fo.write(line)
    line = fi.readline()

fi.close()
fo.close()
