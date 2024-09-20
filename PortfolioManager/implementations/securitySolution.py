# Uncomment the above line and run this cell to save solution

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.securityInterface import securityInterface

"""
The security class defines a security. Each security has a unique identifier
represented by its name.
"""
class security(securityInterface):
    """
    Initializes a new security.

    Arguments:
        `name` The name of the security.
    """
    def __init__(self, name: str):
        self.name = name

    """
    Gets the name of the security

    Returns:
        The name of the security.
    """
    def getName(self) -> str:
        return self.name

    """
    Outputs the security in string format.

    Returns:
        The security's string representation.
    """
    def __str__(self) -> str:
        s = "Security name: " + self.name
        return s

    def __eq__(self, other) -> bool:
        if isinstance(other, securityInterface):
            return self.name == other.getName()
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    __hash__ = object.__hash__

