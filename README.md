pdns-qof-server
===============

pdns-qof server [qof](https://github.com/adulau/pdns-qof) compliant passive DNS query interface for the [pdns-toolkit](https://github.com/adulau/pdns-toolkit) or similar passive dns.

Requirements
------------

- Python 3
- [Tornado](http://www.tornadoweb.org)
- Python [iptools](https://github.com/bd808/python-iptools)
- Python [redis](https://pypi.python.org/pypi/redis/) client

Running the qof-server
----------------------

The server is using the default Redis configuration for the pdns-toolkit. Don't forget to change it if you have different
configuration for your Passive dns data store.

```bash
python3 ./bin/qos-server.py
```

Usage
-----

```bash
curl http://127.0.0.1:8888/query/www.microsoft.com
```

```json
{"count": "126595", "time_first": "1298398002", "rrtype": "CNAME", "rrname": "www.microsoft.com", "rrdata": "toggle.www.ms.akadns.net", "time_last": "1387960200"}
```
```bash
curl http://127.0.0.1:8888/query/80.169.63.162
```

```json
{"count": "112", "time_first": "1298398002", "rrtype": "A", "rrname": "infosports.dhnet.be", "rrdata": "212.35.116.234", "time_last": "1354530214"}
{"count": "4", "time_first": "1361180820", "rrtype": "A", "rrname": "infosports.dh.be", "rrdata": "80.169.63.162", "time_last": "1366210757"}
{"count": "2", "time_first": "1357803074", "rrtype": "A", "rrname": "maintenance.lalibre.be", "rrdata": "212.35.116.249", "time_last": "1357803074"}
{"count": "48", "time_first": "1374008604", "rrtype": "A", "rrname": "s.llb.be", "rrdata": "80.169.63.162", "time_last": "1384916107"}
{"count": "94256", "time_first": "1298398002", "rrtype": "A", "rrname": "www.lalibre.be", "rrdata": "212.35.116.249", "time_last": "1361278027"}
{"count": "213", "time_first": "1298398834", "rrtype": "A", "rrname": "infosports.lalibre.be", "rrdata": "212.35.116.234", "time_last": "1355432823"}
```

rr-types tool
-------------

rr-types.py is a tool to dump current IANA DNS RR types in various formats.

```bash
python3 bin/rr-types.py --help
usage: rr-types.py [-h] [-d] [-j] [-i] [-v]

Dump IANA DNS parameters in various formats

optional arguments:
  -h, --help  show this help message and exit
  -d          Python dict
  -j          JSON output (default format)
  -i          Disable integer value RR check
  -v          Verbose output
```

