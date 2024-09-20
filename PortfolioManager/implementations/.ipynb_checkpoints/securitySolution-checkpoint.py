#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

"""
Allow for the name of a security to be stored on object construction & via a setter function
Allow for the name of the security to be retrieved via a getter
"""
class Security(SecurityInterface):
    def __init__(self, security_name: str):
        self.security_name = security_name

    def get_security_name():
        return self.security_name
    
