# --*-- coding: utf-8 --*--

import datetime
import functools
import logging
from exceptions import RateExcceed, APIClosed, AccessForbidden, SignatureInvalid
from configs import API_OPEN_TIME, IP_WHITE_LIST, TRANSPORT_APP_KEY, TRANSPORT_APP_SECRET
from signature import Signature

def api_rate_limit(mode="seperate", interval=1):
    def decorator(fn, *args, **kwargs):
        @functools.wraps(fn)
        async def inner(self, request, *args, **kwargs):

            #验证签名
            signaure_valid = Signature.verify(TRANSPORT_APP_KEY,
                                              TRANSPORT_APP_SECRET,
                                              request.headers.get('app-nonstr', ''),
                                              request.headers.get('app-timestamp', ''),
                                              request.headers.get('app-signature', ''))
            if not signaure_valid:
                raise SignatureInvalid("signature invalid!")

            #验证ip白名单
            remote_ip = request.headers.get("X-FORWARDED-FOR", None)
            logging.debug("[peername] " + str(request.transport.get_extra_info('peername')))
            if remote_ip not in IP_WHITE_LIST:
                peername = request.transport.get_extra_info('peername')
                if peername is not None:
                    host, port = peername
                    if host not in IP_WHITE_LIST:
                        raise AccessForbidden("who are you?")
                else:
                    raise AccessForbidden("who are you?")

            #验证可访问时间
            dt = datetime.datetime.now()
            if dt.time() < datetime.time(API_OPEN_TIME[0]) or dt.time() > datetime.time(API_OPEN_TIME[1]):
                raise APIClosed("we are closed!")

            #验证访问频率
            key = ""
            if mode == "seperate":
                key = request.path
            else:
                key = "rate_limit_key"
            exist = await request.app['redis'].exists(key)
            if exist:
                raise RateExcceed("api request too fast")

            resp = await fn(self, request)
            await request.app['redis'].set(key, '', expire=interval, exist=True)
            return resp
        return inner
    return decorator