#!/usr/bin/python

"""
#############
permisos python
https://stackoverflow.com/questions/12168110/how-to-set-folder-permissions-in-windows/43244697#43244697

$ python3 ./create_folder_with_link.py
bash: /c/Users/Jonathan/AppData/Local/Microsoft/WindowsApps/python3: Permission denied


#############
ModuleNotFoundError: No module named 'win32security'
https://stackoverflow.com/questions/27547435/how-to-find-import-the-win32security-in-python

https://pypi.org/project/pywin32/
----------------------------------------------------
"""

import win32security
import ntsecuritycon as con

FILENAME = "create_folder_with_link.py"

userx, domain, type = win32security.LookupAccountName ("", "Jonathan")
usery, domain, type = win32security.LookupAccountName ("", "Jonathan")

sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()

dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, usery)

sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)