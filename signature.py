from hashlib import md5
import base64
import random
import string
import time


class Signature():

    @classmethod
    def verify(cls, app_key, app_secret, randam_str, timestamp_str, signature):
        """
        验证签名
        :param app_key:
        :param app_secret:
        :param randam_str:
        :param timestamp_str:
        :param signature:
        :return:
        """
        if not timestamp_str:
            return False
        if time.time()*1000 - float(timestamp_str) > 5*60*1000:
            return False

        m = md5()
        s = '%s:%s:%s:%s' % (app_key, app_secret, randam_str, timestamp_str)
        m.update(bytes(s.encode('utf-8')))
        return m.hexdigest() == signature

# m = md5()
# t = str(time.time()*1000)
# print(t)
# s = '%s:%s:%s:%s' % ("tzGa99gCem1qw6AZF7tJXKia", "l6x99AEhO7Mgk6ZQysRmuDCZ", "abc", t)

# # print(md5(s.encode('utf-8')), '222222')
# m.update(bytes(s.encode('utf-8')))
# print( m.hexdigest())
