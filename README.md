practice project to learn Flask.



TODO:

- current:
  - dependency on setting up config.py
  - http://flask.pocoo.org/docs/config/
  - what to do with internal logging?
    - "STUB: logging" e.g. models.py

- network-tools/whois
  - BUG: form submit clash, how to decouple the two submits?
  - tidy up wtf.quickform to put title/form/button on same row.
  - split out logic for jwhois requests out of view.py, models.oy more appropriate?
  - create separate form for domain name whois requests
  - look into custom validators to verify domain name (could be nasty if someone escaped out)
  - jwhois binary location in global config file?
- network-tools/{whois,mtr,dns,telnet,nmap}
  - future features
- login/sessions, only access for authenticated users.
- email alerting of errors?
- DNS management via /dns (backed on database)
- /ping-probe
  - setup pings against arbitrary destinatiosn
  - js to graph latency variations?
- mail management via /mail
  - blacklists/whitelists of domains
  - account management
  - very simple webmail UI?
- url shortener, bitly clone?
- pastebin clone?
- alert/monitor dashboard
  - generic framework for alerting from vps

