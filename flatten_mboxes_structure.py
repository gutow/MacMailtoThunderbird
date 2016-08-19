# By Jonathan Gutow <gutow@uwosh.edu> August 15, 2016.
# Released under the GPL3 opensource license 
# https://www.gnu.org/licenses/licenses.html

# This is the second of two scripts used to convert the exported mailbox
# structure from Apple Mail 8.1 - 9.3 (probalby works with later versions too)
# into a format that matches the mbox format used by Thunderbird.

# This script should be run after the first script "fix_mv_mbox.py" has been
# used manually to convert all directories you want to keep.  Then is can be
# run at the root of the mailbox directory structure to flatten and directories
# inside of the ones that were converted.

# Warning: Depending upon how many versions of Apple Mail you have gone through
# this may create multiple duplicate messages in the flattened mailbox.  If you
# care you can manually delete them. I did not have the time to figure out how
# or why Apple was duplicating some of my messages. The goal was to convert
# things to a published format so that I can access them long-term.

# Warning: this script has very limited error checking.  Work on a copy of your
# data.

import os, shutil

def intosbd(sbd):
	print ("Entering .sbd directory: "+sbd)
	listing=os.listdir(sbd)
	containssbd = False
	for x in listing:
		basename,ext = os.path.splitext(x)
		if (ext=='.sbd'):
			intosbd(os.path.join(sbd,x))
			containssbd = True
	if not containssbd:
		flatten(sbd)
	return()
	
def flatten(sbd):
	print ("Flattening .sbd directory: "+sbd)
	for root, dirs, files in os.walk(sbd):
		for name in files:
			filepath = os.path.join(root,name)
			filesize = os.path.getsize(filepath)
			shortpath,filename=os.path.split(name)
			if (filename == 'mbox') and (filesize > 0):
				with open(os.path.join(sbd,'flattened_mboxes'), 'a') as outfile:
					with open(filepath) as infile:
						for line in infile:
							outfile.write(line)
# Now clean up the extra directories
	listing=os.listdir(sbd)
	for x in listing:
		todeletepath = os.path.join(sbd,x)
		xbase,xext = os.path.splitext(x)
		if (os.path.isdir(todeletepath)) and (xext!='.sbd'):
			if os.path.exists(todeletepath):
				shutil.rmtree(todeletepath)
	return()


pwd = os.getcwd()
# Recurse through all directories below the one this script is running in and
# copy any mailbox data found into a single mailbox in each .sbd directory.

intosbd(pwd)
	

