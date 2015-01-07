Procs: Python, Processes, and... Pipes
======================================

Python's Subprocess module is well designed for lower functions. Pipes is designed
to encourage higher functions.


Ideas
-----

- Simple shelling out, allow argument seperation.
- command timeouts
- Process monitoring
- programatically compose a chain of streams.
- process call timeouts

Usage
-----

Simple Usage::

    >>> import procs

    >>> c = procs.run('uptime')
    >>> c.returncode
    0
    >>> c.ok
    True
    >>> print c.stdout
    16:08  up  1:16, 7 users, load averages: 1.02 1.90 1.75


Advanced Usage::

    >>> ls = procs.Process('ls /usr/bin')
    >>> grep = procs.Process('grep python')
    >>> wc = procs.Process('wc -l')
    >>> chain = ls | grep | wc
    >>> chain.run()
    >>> print(chain.stdout)
    19

    >>> from procs import ProcessHandler

    class MyCommmand(ProcessHandler):

        def __init__(self):
            pass

        def on_start(self):
            pass

        def on_exit(self):
            pass

        def on_crash(self):
            pass
