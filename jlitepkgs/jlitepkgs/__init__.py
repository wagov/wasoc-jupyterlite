import js
from requests import request
import pyodide_http
import pandas

pyodide_http.patch_all()

def http_call(path: str, method: str = "GET", **kwargs):
    # Assumes https://github.com/wagov/siem-query-utils/blob/main/siem_query_utils/proxy.py mounted at /proxy
    return request(url=f"{js.origin}/proxy/{path}", method=method, **kwargs)


def kql2df(kql, workspace: str = None, timespan="P1D"):
    # Assumes https://github.com/wagov/siem-query-utils/blob/main/siem_query_utils/api.py mounted at /api/v1
    params = {"query": kql, "timespan": timespan}
    path = "/api/v1/globalQuery"
    if workspace:
        path = "/api/v1/simpleQuery"
        params["name"] = workspace
    response = http_call(path, params=params)
    return pandas.DataFrame(response.json())
