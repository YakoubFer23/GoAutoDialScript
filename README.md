# GoAutoDialScript
Script to automate adding and deleting users/phones in the GoAutoDial CRM
# Usage 
python addUser.py [SERVER_IP] [OPTIONS]
  OPTIONS: 
  1: Add Users (Include usersToAdd.txt)
  2: Delete Users (Include usersToDelete.txt)
  3: Delete Phones (Include phonesToDelete.txt)
  
-usersToAdd.txt format : 
  One Fullname per line (FIRSTNAME LASTNAME).
-usersToDelete.txt format :
  One username per line.
-phonesToDelete.txt
  One phone per line.
# To Implement
-Import Data from a csv file
-Consider edge cases in Fullnames
