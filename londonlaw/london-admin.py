#!/usr/bin/env python

#  London Law -- a networked manhunting board game
#  Copyright (C) 2003-2004, 2005 Paul Pelzl
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License, Version 2, as 
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


from twisted.python import threadable
threadable.init()
import os, gettext, sys

try:
   import adminclient
#   gettext.install("londonlaw") # use system locale dir if client was installed
   cwd=os.getcwd()
#    print("Pfad="+cwd+"\n")
   gettext.install("londonlaw",cwd+"/londonlaw/locale") # use system locale dir if client was installed
   
except:
   gettext.install("londonlaw", "locale") # use local locale directory if launching locally
#   print (_("Attempting to launch admin client from current directory...")).encode(sys.stdout.encoding, "replace")
   print (_("Attempting to launch admin client from current directory..."))
   import sys, os.path
   # add the parent directory to PYTHONPATH
   cwd = os.path.split(os.path.abspath(os.getcwd()))
   sys.path.append(cwd[0])
   import adminclient

adminclient.init()


