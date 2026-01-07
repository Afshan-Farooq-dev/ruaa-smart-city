import inspect
import httpx
print('httpx version:', getattr(httpx, '__version__', 'unknown'))
print('httpx.Client signature:', inspect.signature(httpx.Client))
try:
    import httpx._client as _c
    print('httpx._client.Client signature:', inspect.signature(_c.Client))
except Exception as e:
    print('error reading _client:', e)
