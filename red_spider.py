# coding:utf-8
import requests

RHEL7_URL = "https://access.redhat.com/downloads/content/rhel---7.4/x86_64/4118/kernel/3.10.0-693.39.1.el7/src/fd431d51/package-changelog"
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
ACCOUNT = "rd.sangfor@gmail.com"
PASSWORD = "@Sangfor123"
LOGIN_URL = "https://access.redhat.com/login"

session_obj = requests.Session()

cookie = "AMCV_945D02BE532957400A490D4C%40AdobeOrg=1075005958%7CMCIDTS%7C18438%7CMCMID%7C82003676918387863752493917972296693878%7CMCAAMLH-1593596380%7C11%7CMCAAMB-1593596380%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1592998780s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18445%7CvVersion%7C4.4.1%7CMCCIDH%7C-1362207722; check=true; mbox=session#d10fec924fb0452ea04885cd3b82ae03#1592993424|PC#d10fec924fb0452ea04885cd3b82ae03.38_0#1656235725; rh_omni_tc=701f2000001Css5AAC; AMCVS_945D02BE532957400A490D4C%40AdobeOrg=1; dtm_prevURL=https%3A%2F%2Fsso.redhat.com%2Fauth%2Frealms%2Fredhat-external%2Fprotocol%2Fopenid-connect%2Fauth%3Fclient_id%3Dcustomer-portal%26redirect_uri%3Dhttps%253A%252F%252Faccess.redhat.com%252Fwebassets%252Favalon%252Fj%252Fincludes%252Fsession%252Fscribe%252F%253FredirectTo%253Dhttps%25253A%25252F%25252Faccess.redhat.com%26state%3Dcac0c2be-0c02-4c80-860b-6772387a4c45%26nonce%3D201b7800-78cc-4e4e-8600-5651fc326287%26response_mode%3Dfragment%26response_type%3Dcode%26scope%3Dopenid; sat_prevInternalCampaign=; dtm_prevProp=%7Caccess.redhat.com; sat_prevExtCmp=no%20value; sat_prevUrl=https%3A%2F%2Fsso.redhat.com%2Fauth%2Frealms%2Fredhat-external%2Fprotocol%2Fopenid-connect%2Fauth%3Fclient_id%3Dcustomer-portal%26redirect_uri%3Dhttps%253A%252F%252Faccess.redhat.com%252Fwebassets%252Favalon%252Fj%252Fincludes%252Fsession%252Fscribe%252F%253FredirectTo%253Dhttps%25253A%25252F%25252Faccess.redhat.com%26state%3Dcac0c2be-0c02-4c80-860b-6772387a4c45%26nonce%3D201b7800-78cc-4e4e-8600-5651fc326287%26response_mode%3Dfragment%26response_type%3Dcode%26scope%3Dopenid; sat_prevPage=SSO%7Cauth%7Crealms%7Credhat-external%7Cprotocol%7Copenid-connect%7Cauth; scCidHist=701f2000001Css5AAC; s_cc=true; s_sq=%5B%5BB%5D%5D; rh_user=rd.sangfor|rd|P|; rh_locale=zh_CN; rh_user_id=51768269; rh_sso_session=1; BIGipServer~prod~staticweb-webapp-http=778306826.20480.0000; rh_jwt=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICItNGVsY19WZE5fV3NPVVlmMkc0UXhyOEdjd0l4X0t0WFVDaXRhdExLbEx3In0.eyJqdGkiOiJlZjk3NTQ1Ny0xNGJmLTQ2M2YtYTZlMy0xZDU4ZjYxZmFlNWYiLCJleHAiOjE1OTI5OTE5MTMsIm5iZiI6MCwiaWF0IjoxNTkyOTkxMDEzLCJpc3MiOiJodHRwczovL3Nzby5yZWRoYXQuY29tL2F1dGgvcmVhbG1zL3JlZGhhdC1leHRlcm5hbCIsImF1ZCI6ImN1c3RvbWVyLXBvcnRhbCIsInN1YiI6ImY6NTI4ZDc2ZmYtZjcwOC00M2VkLThjZDUtZmUxNmY0ZmUwY2U2OnJkLnNhbmdmb3IiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjdXN0b21lci1wb3J0YWwiLCJub25jZSI6ImU5MjNjZTMxLTBmYjYtNDRhZi1hZjNiLTlmZTI0N2FiYTZhMiIsImF1dGhfdGltZSI6MTU5Mjk5MDk0NCwic2Vzc2lvbl9zdGF0ZSI6ImZjNWM3NmY0LWUzYzQtNGZjOS05Zjk0LWRmMTY2MDM4NmYxNCIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9wcm9kLmZvby5yZWRoYXQuY29tOjEzMzciLCJodHRwczovL3d3dy5yZWRoYXQuY29tIiwiaHR0cHM6Ly9hY2Nlc3MucmVkaGF0LmNvbSJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiYXV0aGVudGljYXRlZCIsImNhbmRsZXBpbl9zeXN0ZW1fYWNjZXNzX3ZpZXdfZWRpdF9wZXJzb25hbCIsImlkcF9hdXRoZW50aWNhdGVkIiwicG9ydGFsX21hbmFnZV9zdWJzY3JpcHRpb25zIiwiZXJyYXRhOm5vdGlmaWNhdGlvbl9zdGF0dXNfZW5hYmxlZCIsImVycmF0YTpub3RpZmljYXRpb25fZGVsaXZlcnlfd2Vla2x5IiwicG9ydGFsX21hbmFnZV9jYXNlcyIsImVycmF0YTpub3RpZmljYXRpb246c2VjdXJpdHkiLCJlcnJhdGE6bm90aWZpY2F0aW9uX2xldmVsX3N5c3RlbS12aXNpYmxlIiwiZXJyYXRhOm5vdGlmaWNhdGlvbjpidWdmaXgiLCJhZG1pbjpvcmc6YWxsIiwidW1hX2F1dGhvcml6YXRpb24iLCJwb3J0YWxfc3lzdGVtX21hbmFnZW1lbnQiLCJyaGRfYWNjZXNzX21pZGRsZXdhcmUiLCJwb3J0YWxfZG93bmxvYWQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJyaGQtZG0iOnsicm9sZXMiOlsicmh1c2VyIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJSRURIQVRfTE9HSU4iOiJyZC5zYW5nZm9yIiwibGFzdE5hbWUiOiJzYW5nZm9yIiwiY291bnRyeSI6IkNOIiwiYWNjb3VudF9udW1iZXIiOiI2MDgwMjc3IiwicHJlZmVycmVkX3VzZXJuYW1lIjoicmQuc2FuZ2ZvciIsImZpcnN0TmFtZSI6InJkIiwiYWNjb3VudF9pZCI6IjExNzI4MTc4IiwidXNlcl9pZCI6IjUxNzY4MjY5Iiwib3JnYW5pemF0aW9uX2lkIjoiMDBEbTAwMDAwMDAxMTZDIiwic2l0ZUlkIjoicmVkaGF0Iiwic2l0ZUlEIjoicmVkaGF0IiwicG9ydGFsX2lkIjoiMDYwNjAwMDAwMDBEMGFmIiwibGFuZyI6InpoX0NOIiwicmVnaW9uIjoiQ04iLCJlbWFpbCI6InJkLnNhbmdmb3JAZ21haWwuY29tIiwiUkhBVF9MT0dJTiI6InJkLnNhbmdmb3IiLCJ1c2VybmFtZSI6InJkLnNhbmdmb3IifQ.3-uZcLaIxZZgnjhq7mTGLOFJT9z8GNbh9DNAop60hBt8Ppjmsohziod3Bvm2e8RwLmf3mXlrsvz428zoyZEFmDVfGqlTBAPhaIpJrwiBGSwjP-blpK27blCQYHIOs4qceD9wTA68x8pLjCkUx2YxtynUS6CTEKBfr-SJcW9SAgGoYXKmLlv4YAqkd4wRBR3zImjAid-Ux0xKuszCrEtnzeuYSkmjEg0HrucTogmvMAQQ4eDN8BZw6UDJ4M10cER1nr8SI1iZmCpSbunii_ZrIwuv75QMiWmDrq0OJzKmxgle_qEBlrQlgV_WS5MoxoAOSJAyXBpNLt0-o55TtREJnUGvZ9uuw6Rkp6XgyMSA6Wg39FW8wLRpqBAckBPMAvs5zPmc_BxDel2rMW631S6TwG3EILuyu0Ja8VbS3Fq2NhxnKNbv995l7Yuc98pSZexQBQTuIpXj-gjZGOGmuXglPdVhQnuSloSFnxSAwwA8tMbKMqiGyS28jZdCfqIPpaAVd9WFkpEz0LJKw2yu_VDG1WZDMs9-Zm0kqLkAl98rmX6gR37ZAuphlp_0vn8-wI4pujeGeFBanrtT2T-4HHbAnLxvZOmq07FXkiDWuYLPlZiWJlAcPQiQGMds51lsnyzfqdflDhfg_8ZaZxmqaG87HFFDcecEGYnm0uLKnI_CwYE; chrome_session_id=172550|1592990949049; 5de2ca7b93a8fe2d480b8245a8f255a2=84a9dcd9b7fce6c671b8775604c89118; redhat_www_eu_cookie=true; _redhat_downloads_session=XCRkFUgYcisO2jeZ5ze16YUeBgMn1pFxGMSguFWTpljG%2BuDsuCtGEUjE3zI3NexDclKifuN7RlvtF5AvcicApWUiHdLbby0qZVUfPWLvO5326iQc1I7PlGzYqZfSSilD4lnNM%2BKjD4U9m68QQZDOrNRlC9L9TW2y03LNt9dOwCclVG28kAcD%2BDbm7l%2FvtNDOCnNQe9LvItQYkG3JgB0%3D--cPVzG0LMKpVlF6g3--gYdqyQsUK1HtfwkSQFQq%2Bg%3D%3D; 687975abb031448267d67b8718cb78ea=3bdbc168c2682a7092bab2d2167a5ecb; sat_ppv=13; dtm_cpReg=yes"

headers = {
    "User-Agent": USER_AGENT,
    "Cookie": cookie,
    # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    # "Upgrade-Insecure-Requests": "1"

}

response = session_obj.get(RHEL7_URL, headers=headers)

if response.status_code == 200:
    with open("red.txt", "w", encoding="utf-8", errors="ignore") as fp:
        fp.write(response.text)
