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
- >>> uptime.stdout >> cowsay.stdin

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

    >>> chain = procs.chain()
    >>> uptime = chain.process('uptime')
    >>> cowsay = chain.process('cowsay')
    >>> chain.link(uptime.stdout, cowsay.stdin)
    >>> chain.start(wait=True)
    >>> chain.wait()


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
