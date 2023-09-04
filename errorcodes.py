#--*-- coding: utf-8 --*--

from enum import Enum  # Needs package enum34
from enum import unique


@unique
class ErrorCodes(Enum):
    Ok = 0
    RATEEXCCEED = 40000
    APICLOSED = 40001
    ACCESSFORBIDDEN = 40003
    SIGNATUREINVALID = 40004


    ResourceExist = 201
    UnAuthorized = 403
    UnAuthenticated = 401
    ResourceNotExist = 404
    MethodNotAllowed = 405
    Forbidden = 0xFFFFFFFE
    DeviceHasBeenBanned = 0xFFFFFFFF
    BadRequest = 0x80000000
    InternalServerError = 0x7FFFFFFF
    #add more when needed
