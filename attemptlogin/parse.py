#!/usr/bin/env python3

import re


counter = 0 # we will use this to count failed logins


## open our log file (read mode)
myfile = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')
myoutput = open('/home/student/mycode/attemptlogin/failed.dat', 'w')

myfilelist = myfile.readlines()

## scan log for number of failed logins


for a_single_line in myfilelist:
  if "failed" in a_single_line:
    counter = counter + 1
    ## counter += 1 ## This would do the same thing as the above line
    print(a_single_line)
    print(a_single_line, myoutput)
    mymatchobj = re.search(r'(failed.)(.*)from/s+(.*$)', a_single_line)
    print("the failure reasn is: ", mymatchobj.group(2), " The IP of te offender is : ", mymatchobj.group(3))
    print(mymatchobj.group(3), file=bannedIPs)


## print data to the user
print("Total number of failures: ", counter)

bannedIPs.close()
myfile.close()
myoutput.close()
