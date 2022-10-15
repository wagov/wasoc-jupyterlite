import js
from requests import request
import pyodide_http
import pandas

pyodide_http.patch_all()

def http_call(path: str, method: str = "GET", **kwargs):
    return request(url=f"{js.origin}/{path}", method=method, **kwargs)


def kql2df(kql, workspace: str = None, timespan="P1D"):
    params = {"query": kql, "timespan": timespan}
    path = "/siemqueryutils/api/v1/globalQuery"
    if workspace:
        path = "/siemqueryutils/api/v1/simpleQuery"
        params["name"] = workspace
    response = http_call(path, params=params)
    return pandas.DataFrame(response.json())
