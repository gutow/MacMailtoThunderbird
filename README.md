# MacMailtoThunderbird
Python scripts to help convert Mac Mail Export to Thunderbird mbox format.

By Jonathan Gutow <gutow@uwosh.edu> August 15, 2016.
Released under the GPL3 opensource license 
https://www.gnu.org/licenses/licenses.html

* Warning: These scripts have very limited error checking.  Work on a copy of your data.*

* How to use:*
1. Within Apple Mail select the mail folder or folders you wish to export.
2. Using the right-click or "Message" menu select "Export...".
3. In the "Save" dialog that appears click on "Options" and select "include folders".
4. Create a new folder to save into and then save.
5. Copy these two scripts into the same folder for convenience or to a location easily specified on the command line.
6. Open a terminal and use the "cd"  (change directory) command to navigate to where you stored the the export (e.g. `cd /Users/yourname/Documents/mail_export`).
7. Run the first script: `python fix_mv_mbox.py`.
8. Navigate into the folder structure using the `cd` command. Within each folder that you wish to appear as a folder in the import rerun the first script: `python /Users/yourname/Documents/mail_export/fix_mv_mbox.py`. Folders below the lowest level you run this script in will be flattened into one mailbox later.
9. 


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

This is the second of two scripts used to convert the exported mailbox
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
