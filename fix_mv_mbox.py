# By Jonathan Gutow <gutow@uwosh.edu> August 15, 2016.
# Released under the GPL3 opensource license 
# https://www.gnu.org/licenses/licenses.html

# This script is the first of two meant to be used together.
# This script is designed to convert the pseudo mbox export of Apple Mail 8.1 -
# 9.3 (probably works with newer versions too) to the mbox format used by
# Thunderbird.  This allows you to move sorted local mailboxes from Apple Mail
# to Thunderbird without completely destroying the organization.

#This script does not recurse through directories.  It only adjusts the .mbox
# directories, organizational folders and mboxes at the first level of the 
# present working directory to the Thunberbird format.  If you wish to adjust
# directories at lower levels you need to manually change to the next lower
# level and rerun this script.  Within any directory that is meant to be the
# lowest level the second script "flatten_mboxes_structure.py" should be run to
# compact the additional hidden levels that Apple Mail has created.

# Warning: this script has very limited error checking.  Work on a copy of your
# data.

import os, shutil

pwd = os.getcwd()
listing=os.listdir(pwd)
mboxdirs=[]
# Get a listing of this directory and figure out which are Apple folder versions
# of mboxes.  Convert other types of directories to directories with the '.sbd'
# extension used by Thunderbird.
for x in listing:
	basename,ext=os.path.splitext(x)
	if (ext=='.mbox'):
		mboxdirs.append(x)
	if ((ext!='.sbd') and (ext!='.mbox')) and os.path.isdir(x):
	    fullpath=os.path.join(pwd,x)
	    os.rename(fullpath,fullpath+'.sbd')
# Convert the Apple folder versions of mboxes into Thunderbird mboxes and then
# delete the unnecessary directories.
for x in mboxdirs:
	oldmboxname = os.path.join(pwd,x,'mbox')
	basename,ext=os.path.splitext(x)
	newmboxname = os.path.join(pwd,basename)
	mboxdirpath=os.path.join(pwd,x)
	if (os.path.isdir(mboxdirpath)):
		if (os.path.exists(oldmboxname)):
			os.rename(oldmboxname,newmboxname)
		if (os.path.exists(mboxdirpath)):
			shutil.rmtree(mboxdirpath)