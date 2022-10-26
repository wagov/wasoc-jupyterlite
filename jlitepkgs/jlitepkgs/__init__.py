import js
from requests import request
import pyodide_http
import pandas

pyodide_http.patch_all()

def http_call(path: str, method: str = "GET", **kwargs):
    # Assumes https://github.com/wagov/siem-query-utils/blob/main/siem_query_utils/proxy.py mounted at /proxy
    return request(url=f"{js.origin}/proxy/{path}", method=method, **kwargs)


def kql2df(kql, timespan="P1D"):
    # Assumes https://github.com/wagov/siem-query-utils/blob/main/siem_query_utils/api.py mounted at /api/v1
    params = {"timespan": timespan}
    path = "/api/v2/query"
    response = request(url=f"{js.origin}{path}", method="POST", params=params, data=kql)
    return pandas.DataFrame(response.json())
