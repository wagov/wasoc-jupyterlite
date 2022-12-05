import js
from requests import request
import pyodide_http
import pandas

pyodide_http.patch_all()

def http_call(path: str, method: str = "GET", **kwargs):
    # Assumes https://github.com/wagov/siem-query-utils/blob/main/siem_query_utils/proxy.py mounted at /
    return request(url=f"{js.origin}/{path}", method=method, **kwargs)
