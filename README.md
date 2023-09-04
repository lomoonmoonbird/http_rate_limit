# http_rate_limit
HTTP限制，包括签名验证，IP白名单，API开放时间，API速度限制

# usage

## 接口速率

接口请求1s间隔
```python
@api_rate_limit(interval=1)
    async def exercise_delta(self, request):
```

## 签名验证

签名在http header中通过app-nonstr,app-timestamp,app-signature三个参数和引用的key，secret进行验证

## IP白名单

IP白名单通过配置文件IP_WHITE_LIST与http header中的X-FORWARDED-FOR进行验证

## 合法时效

通过配置文件API_OPEN_TIME及当前时间验证是否在合法时间内
