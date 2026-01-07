import traceback
from groq import Groq
import httpx

try:
    http_client = httpx.Client()
    client = Groq(api_key='test', http_client=http_client)
    print('Groq client created:', type(client))
except Exception:
    traceback.print_exc()
