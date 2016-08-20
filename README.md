# MacMailtoThunderbird
Python scripts to help convert Mac Mail Export to Thunderbird mbox format. These were written because none of the standard suggested procedures I found searching the web as of August 2016 worked with the output of Apple Mail 8.1 +.

By Jonathan Gutow <gutow@uwosh.edu> August 15, 2016.
Released under the GPL3 opensource license 
https://www.gnu.org/licenses/licenses.html

**Warning: These scripts have very limited error checking. Work on a copy of your data.**

**How to use:**

1. Within Apple Mail select the mail folder or folders you wish to export.
2. Using the right-click or "Message" menu select "Export...".
3. In the "Save" dialog that appears click on "Options" and select "include subfolders".
4. Create a new folder to save into and then save.
5. Copy these two scripts into the same folder for convenience or to a location easily specified on the command line.
6. Open a terminal and use the "cd"  (change directory) command to navigate to where you stored the the export (e.g. `cd /Users/yourname/Documents/mail_export`).
7. Run the first script: `python fix_mv_mbox.py`.
8. Navigate into the folder structure using the `cd` command. Within each folder that you wish to appear as a folder in the import rerun the first script: `python /Users/yourname/Documents/mail_export/fix_mv_mbox.py`. Folders below the lowest level you run this script in will be flattened into one mailbox later.
9. After you have navigated through the directory and run the first script in every folder you wish to appear in the export, navigate back to the root of the export: `cd /Users/yourname/Documents/mail_export`.
10. In this folder run the second script `python flatten_mboxes_structure.py`.  This will compress any lower mailboxes you did not run the first script in into single mailboxes within the lowest level folder you did run the first script in.  The reason for this is that Apple Mail creates all kinds of book-keeping directories.  You may get duplicate e-mails because I did not figure out how to tell which folders contained duplicates only for record keeping.
11. The folder structure may now be imported into Thunderbird as follows:
 1. Make sure Thunderbird is not running.
 2. Navigate to your home folder.
 3. On MacOS you need to open the "Library" folder which is hidden.  There are many ways of doing this.  Search the web as things periodically change depending upong the OS version.
 4. Within the "Library" folder find the "Thunderbird" Folder.  Bore down in this folder to "Thunderbird/Profiles/XXX.default/Mail/Local Folders".
 5. Copy the fixed mailbox directory structure into this folder.
 6. Start Thunderbird.  Your mail should now appear.  Information about what has been read will be lost.  You will need to reset all these mailboxes to read,if that is what they were.

More details of the scripts and their usage can be found in the comments contained in the scripts.

Report issues in the [issue tracker](https://github.com/gutow/MacMailtoThunderbird/issues).
