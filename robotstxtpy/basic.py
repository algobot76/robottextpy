#!/bin/env python3

import os 

def writeInput():
    ep = input("Enter endpoint.\n")
    st = input("Allow or disallow. Enter yes or no.\n")
    if st == 'yes':
        flag = 1
    elif st == 'no':
        flag = 0
    else:
        print("invalid response")
        writeInput()


    allow = {1: "Allow: ", 0: "Disallow: "}
    # if file not exist
    # write User-agent: *
    myfile = open("endpoints.txt", "a+")
    statinfo = os.stat("endpoints.txt")
    if statinfo.st_size == 0:
        myfile.write("User-agent: *\n")
    else:
        pass
    
    myfile.write(allow[flag]+ep+'\n')
        


def main():
    stop = 0
    while not stop:
        writeInput()
        st = input("stop? yes or no.\n")
        if st == "yes":
            stop = 1
        else:
            pass

if __name__ == "__main__":
    main()

