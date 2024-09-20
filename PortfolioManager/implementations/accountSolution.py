# Uncomment the above line and run this cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from typing import Set, Iterable, Dict, Any
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from interfaces.accountInterface import accountInterface
from implementations.securitySolution import security as securityObject

"""
[*] Allow for an account to be created with a set of positions and an account name
[*] Allow for querying of the current account's name
[*] Allow for the querying of all positions
Allow for querying of positions with a set of security names/security objects
The set can contain both security name string and security objects
The return value should be a map with the query value to the position
The set can contain securities not present in the account. These should be ignored.
Allow for positions to be added to the account with a set of position objects. Incoming positions should update existing positions
Allow for the removal of positions from the account with a set of security names/security objects. Securities not in the account should be ignored.

It goes account -> position -> security
"""
class account(accountInterface):
    """
    Initialize the account.

    Args:
        positions The set of positions associated with the account
        accountName The name of the account
    """
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.positions = positions
        self.accountName = accountName

    """
    Query the current account's name.

    Returns:
        The accountName associated with this account
    """
    def getName(self) -> str:
        return self.accountName

    """
    Query all positions.

    Returns:
        A set containing all positions associated with this account
    """
    def getAllPositions(self) -> Iterable[positionInterface]:
        return self.positions.copy()

    """
    Return a map of positions given a set of securities.

    Allow for querying of positions with a set of security names/security objects
    The set can contain both security name string and security objects
    The return value should be a map with the query value to the position
    The set can contain securities not present in the account. These should be ignored.
    """
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        position_map = dict()

        for position in self.positions:
            if position.getSecurity() in securities:
                position_map[position.getSecurity()] = position
            if position.getSecurity().getName() in securities:
                position_map[position.getSecurity().getName()] = position
        
        return position_map
        
    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    def removePositions(self, securities: Set) -> None:
        pass


