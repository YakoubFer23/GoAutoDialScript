import requests
import getpass
from requests.auth import HTTPBasicAuth
import random
import string
import sys

if len(sys.argv) != 3 :
    print('Usage : python addUser.py [SERVER_IP] [OPTIONS]\n\rOPTIONS: \n\r1:Add Users (Include usersToAdd.txt)\n\r2:Delete Users (Include usersToDelete.txt)\n\r3:Delete Phones (Include phonesToDelete.txt)')
    sys.exit()

server_ip = sys.argv[1]

userName= input('Enter user name: ')
password = getpass.getpass()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

basic = HTTPBasicAuth(userName, password)
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36' 
}


def addUsers():
    with open('usersToAdd.txt') as usersToAdd:
        for line in usersToAdd:
            userFullName = line.strip('\n')
            splitname = line.split(" ",1)
            username = splitname[1][0] + splitname[0]
            username = username.lower()
            pswrd = get_random_string(8)
            # username = line.strip('\n')
            # print(userFullName + ' ' +  username)
            data = {
                'ADD': 2,
                'user_toggle': 0,
                'user': username,
                'pass': pswrd,
                'full_name': userFullName,
                'user_level': 1,
                'user_group': 'AGENTS',
                }
            r = requests.post('http://' + server_ip + '/vicidial/admin.php', data=data, verify=False, headers=headers, auth=basic)
            if "USER ADDED" in r.text:
                print(username + " User Added")
            else:
                print(username + " User Not Added")

def deleteUsers():
    with open('usersToDelete.txt') as userstoDelete:
        for user in userstoDelete:
            user = user.strip('\n')
            #print(user)
            url = 'http://' + server_ip + '/vicidial/admin.php?ADD=6&user=' + user +'&CoNfIrM=YES'
            confirm = 'USER DELETION COMPLETED: ' + user
            r = requests.get(url, verify=False, headers=headers, auth=basic)
            if confirm in r.text:
                print(user + ' Succesfully Deleted')
            else:
                print(user + ' Not Deleted')


def deletePhones():
    with open('phonesToDelete.txt') as phonestoDelete:
        for phone in phonestoDelete:
            phone = phone.strip('\n')
            url = 'http://' + server_ip + '/vicidial/admin.php?ADD=61111111111&extension=' + phone + '&server_ip=' + server_ip + '&CoNfIrM=YES'
            confirm = 'PHONE DELETION COMPLETED: ' + phone + ' - ' + server_ip
            r = requests.get(url,verify=False, headers=headers, auth=basic)
            if confirm in r.text:
                print (phone + ' Succesfully Deleted')
            else:
                print(phone + ' Not Deleted')




if sys.argv[2] == 1 :
    addUsers()
elif sys.argv[2] == 2 :
    deleteUsers()
elif sys.argv[2] == 3 :
    deletePhones()
else :
    print('Usage : python addUser.py [SERVER_IP] [OPTIONS]\n\rOPTIONS: \n\r1:Add Users (Include usersToAdd.txt)\n\r2:Delete Users (Include usersToDelete.txt)\n\r3:Delete Phones (Include phonesToDelete.txt)')
    sys.exit()