pdns-qof-server
===============

pdns-qof compliant passive DNS query interface for the pdns-toolkit

Usage
-----

```bash
curl http://127.0.0.1:8888/query/www.microsoft.com
```

```json
{"count": "126525", "time_first": "1298398002", "rrtype": "CNAME", "rrname": "www.microsoft.com", "rrdata": "toggle.www.ms.akadns.net", "time_last": "1387894724"}
{"count": "126525", "time_first": "1298398002", "rrtype": "CNAME", "rrname": "www.microsoft.com", "rrdata": "toggle.www.ms.akadns.net", "time_last": "1387894724"}
```
