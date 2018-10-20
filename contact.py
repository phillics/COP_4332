#
#   To Start Program:       python contact.py
#   To Quit Program:        quit
#   To Display Help:        help
#   To Create Contact:      add NAME
#   To Delete Contact:      del NAME
#   To Edit Contact:        edit NAME
#
#   To Search Contacts:     search KEY [in ATTRIBUTE]
#           KEY is a string,
#           ATTRIBUTE is one or more of: name, phone, email,
#                   seperated by ::
#   To List Contacts:       list [sort by ATTRIBUTE]
#
#   Stretch Goals:
#   Email
#   Text
#   Reminders
#

import os, sys

def helping():
    print("HOW TO USE:")
    print("Each contact has the following attributes:")
    print("\tNAME PHONE EMAIL GROUP\n")
    print("add NAME\tcreates new contact")
    print("del NAME\tdeletes specified contact")
    print("edit NAME\tedit attributes of specified contact")
    print("search KEY\tsearch for KEY in all contacts")
    print("list\t\tdisplay all contacts")
    print("help\t\tdisplay this page")
    print("quit\t\texit program")

def add(inList = []):
    if len(inList) > 2:
        for name in inList[2:]:
            inList[1] += " " + name
        inList = inList[:2]

    if len(inList) != 2:
        print("ERROR: INVALID USAGE\n\tExpected: add NAME")
    else:
        print("adding " + inList[1] + " to contacts")
        cfile = open("contacts.txt", "a")
        cfile.write(inList[1] + "\n")
        cfile.close()

def delete(inList = []):
    if len(inList) > 2:
        for name in inList[2:]:
            inList[1] += " " + name
        inList = inList[:2]

    if len(inList) != 2:
        print("ERROR: INVALID USAGE\n\tExpected: del NAME")
    else:
        #TODO: Are you sure? show contact to be deleted...

        # copy contents over to tmp file, except line we want to remove

        oldFile = open("contacts.txt", "r")
        newFile = open("tmp.txt", "w")

        for line in oldFile.read().split('\n'):
            # if key is in name, don't copy
            if line.find(inList[1]) == 0:
                continue

            # don't copy empty lines
            if len(line) == 0:
                continue

            newFile.write(line + "\n")

        oldFile.close()
        newFile.close()

        # then delete old file and rename tmp to contacts
        os.remove("contacts.txt")
        os.rename("tmp.txt", "contacts.txt")


def edit(inList = []):
    if len(inList) > 2:
        for name in inList[2:]:
            inList[1] += " " + name
        inList = inList[:2]

    if len(inList) != 2:
        print("ERROR: INVALID USAGE\n\tExpected: edit NAME")
    else:
        # load record to edit
        oldFile = open("contacts.txt", "r")
        newFile = open("tmp.txt", "w")

        for line in oldFile.read().split('\n'):
            if line.find(inList[1]) == 0:
                line = editContact(line.split(':'))
            if len(line) == 0:
                continue

            newFile.write(line + "\n")

        oldFile.close()
        newFile.close()

        # then delete old file and rename tmp to contacts
        os.remove("contacts.txt")
        os.rename("tmp.txt", "contacts.txt")

def editContact(contact = []):
    while True:
        print("Enter number of attribute to change:")
        print("1) Name:\t" + contact[0])
        print("2) Phone:\t" + contact[1])
        print("3) Email:\t" + contact[2])
        print("4) Group:\t" + contact[3])
        print("Enter 0 to save changes")
        print(">>> ", end = '')

        choice = input()

        if choice == '0':
            break;
        elif choice == '1':
            print("Name >>> ", end = '')
            contact[0] = input()
        elif choice == '2':
            print("Phone >>> ", end = '')
            contact[1] = input()
        elif choice == '3':
            print("Email >>> ", end = '')
            contact[2] = input()
        elif choice == '4':
            print("Group >>> ", end = '')
            contact[3] = input()
        else:
            print("ERROR: INVALID CHOICE\n\t")
    retStr = contact[0] + ":" + contact[1] + ":" + contact[2] + ":" + contact[3]
    return retStr


def search(inList = []):
    if len(inList) > 2:
        for name in inList[2:]:
            inList[1] += " " + name
        inList = inList[:2]

    if len(inList) != 2:
        print("ERROR: INVALID USAGE\n\tExpected: search KEY")

    cfile = open("contacts.txt", "r")

    for line in cfile.read().split('\n'):
        if line.find(inList[1]) != -1:
            print(line)
    cfile.close()

def listing():
    cfile = open("contacts.txt", "r")
    print(cfile.read())
    cfile.close()

def cli():
    while True:
        # get user input
        print("#>\t", end = '')
        usrInput = input()

        if len(usrInput) == 0:
            continue

        inList = usrInput.split()
        first = inList[0]

        if first == "quit":
            break
        elif first == "help":
            helping()
        elif first == "add":
            add(inList)
        elif first == "del":
            delete(inList)
        elif first == "edit":
            edit(inList)
        elif first == "search":
            search(inList)
        elif first == "list":
            listing()
        else:
            print("ERROR: UNRECOGNIZED COMMAND.\n\ttype 'help' for options\n")

if __name__ == "__main__":
    cli()
