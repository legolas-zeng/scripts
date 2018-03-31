nginx:
  pkg:
    - installed
  service:
    - running
    - enable: True
    - reload: True
    - watch:
      - pkg: nginx
      - file: /etc/nginx/nginx.conf
      - file: /etc/nginx/vhosts/tornado.conf
/etc/nginx/nginx.conf:
  file.managed:
    - source: salt://etc/nginx/nginx.conf
    - user: root
    - group: root
    - mode: 644
    - name: /etc/nginx/nginx.conf

/etc/nginx/vhosts/tornado.conf:
  file.managed:
    - source: salt://etc/nginx/vhosts/tornado.conf
    - user: root
    - group: root
    - mode: 644
    - name: /etc/nginx/vhosts/tornado.conf