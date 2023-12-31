from multiprocessing import cpu_count

wsgi_app = 'explorer2go.wsgi:application'
access_log_format = '%(h)s %(p)-6s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(M)s "%(f)s" "%(a)s"'   # noqa

loglevel = 'info'
capture_output = False

workers = int(max(cpu_count() / 2, 1))
threads = 4

bind = '0.0.0.0:8000'

accesslog = '-'
errorlog = '-'
