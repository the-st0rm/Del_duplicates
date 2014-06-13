Del_duplicates
==============

A script to delete duplicate files in your hard drive

Introduction: We always download files more than time in different places, such as movies, songs or any other type of data. 
We usually foget where they are and they end up taking a huge space in our hard drives. In my case I managed to remove a 50 Gb of duplicate files.
The Del_duplicate script search the given folder and the children folders for all duplicate files. It then deletes one of the duplicate files and keep the original.
After that it loops over all the folder to check if there are any empty folders. If found, it deletes them. 


How it works:
simply run "python Del_duplicates.py" then type the absoulute path of where the script should start working.


TO-DO:
1) Enhance the exception handling
2) Make the script incremental. So if I ran the script on a folder that contains 500 GB and after a month I run it again, the script doesn't have to calcuate their checksums again
3) Add more options to run the script, such as hashing function.
4) Maybe add a GUI (I don't prefer GUI's though ^^)
