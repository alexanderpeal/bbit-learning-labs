# Uncomment the above line and run this cell to save solution

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from typing import Union
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from implementations.securitySolution import security as securityObject

"""
The position class represents a position. A position is associated with a security and a seed/inital position, and supports
the following operations:

Allows for a position to be created with a security name or object and a seed position value
Allows for gathering of the position's security and position value
Allows for updating of the position's size via addition & setting
"""
class position(positionInterface):
    """
    Initializes a new position.
    """
    def __init__(self, security: Union[str, securityObject], seed: int):
        # If secuirty name is provided to first arg, make new securityObject using that name
        if isinstance(security, str):
            self.security = securityObject(security)
            
        # If security object is provided to first arg, use the existing securityObject
        if isinstance(security, securityObject):
            self.security = security
            
        self.seed = seed

    """
    Gets the securityObject associated with this position.

    Returns:
        The security object associated with the position.
    """
    def getSecurity(self) -> securityObject:
        return self.security

    """
    Gets the seed position value associated with this position.
    """
    def getPosition(self) -> int:
        return self.seed

    """
    Sets the seed position value to newSeed.

    Arguments:
        `newSeed`: The new seed position value.
    """
    def setPosition(self, newSeed: int) -> None:
        if newSeed < 0:
            raise ValueError("Error: The new position seed value resulted in a short position")
        self.seed = newSeed

    """
    Increments the seed position value by `value`. If the new value is negative,
    this method will throw an error.

    Arguments:
        `value`: The value to increase the position by.
    """
    def addPosition(self, value: int) -> None:
        if self.seed + value < 0:
            raise ValueError("Error: The new position seed value resulted in a short position")
            
        self.seed += value

    """
    Outputs the position in string format.

    Returns:
        The position's string representation.
    """
    def __str__(self) -> str:
        s = "Position:\n" + str(self.security) + "\nSeed: " + str(self.seed)
        return s
