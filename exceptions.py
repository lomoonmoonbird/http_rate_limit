from errorcodes import ErrorCodes


class AppException(Exception):
    def __init__(self, error_code, message=''):
        self.code = error_code
        self.message = message


class MysqlConnectionError(AppException):
    def __init__(self, message):
        super(MysqlConnectionError, self).__init__(ErrorCodes.BadRequest, message)

class RequestParamError(AppException):
    def __init__(self, message):
        super(RequestParamError, self).__init__(ErrorCodes.BadRequest, message)

class ResourceNotExist(AppException):
    def __init__(self, message):
        super(ResourceNotExist, self).__init__(ErrorCodes.ResourceNotExist, message)

class ResourceExist(AppException):
    def __init__(self, message):
        super(ResourceExist, self).__init__(ErrorCodes.ResourceExist, message)

class ForbiddenError(AppException):
    def __init__(self, message):
        super(ForbiddenError, self).__init__(ErrorCodes.Forbidden, message)

class MethodNotAllowedError(AppException):
    def __init__(self, message):
        super(MethodNotAllowedError, self).__init__(ErrorCodes.MethodNotAllowed, message)

class CacheHit(AppException):
    def __init__(self, data):
        self.code = ErrorCodes.Ok
        self.message = ''
        self.data = data

class InternalServerError(AppException):
    def __init__(self, message):
        super(InternalServerError, self).__init__(ErrorCodes.InternalServerError, message)


class RateExcceed(AppException):
    def __init__(self, message):
        super(RateExcceed, self).__init__(ErrorCodes.RATEEXCCEED, message)


class APIClosed(AppException):
    def __init__(self, message):
        super(APIClosed, self).__init__(ErrorCodes.APICLOSED, message)

class AccessForbidden(AppException):
    def __init__(self, message):
        super(AccessForbidden, self).__init__(ErrorCodes.ACCESSFORBIDDEN, message)

class SignatureInvalid(AppException):
    def __init__(self, message):
        super(SignatureInvalid, self).__init__(ErrorCodes.SIGNATUREINVALID, message)