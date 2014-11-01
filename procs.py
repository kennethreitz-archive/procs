import os
import subprocess


class Process(object):
    def __init__(self, command):
        self.command = command
        self.environ = {}
        self.cwd = None


    def set_command(self, command):
        # process popen chain, etc
        self.command = command

    def set_environ(self, environ, clean=False):
        self.environ = dict() if clean else dict(os.environ)
        self.environ.update(environ)

    def set_cwd(self, cwd):
        # expand, discover, etc.
        self.cwd = cwd

    def start(self):
        pass

    @property
    def stdin(self):
        return 'stdin'

    @property
    def stdout(self):
        return 'stdout'

    @property
    def stderr(self):
        return 'stderr'


class Chain(object):

    def __init__(self):
        self.processes = []

    def process(self, command):
        p = Process(command)
        self.processes.append(p)

        return p

    def link(self, x, y):
        print 'Linking {} to {}'.format(x, y)

    def start(self, wait=False):
        for process in self.processes:
            process.start()

        self.wait()

    def wait(self):
        # wait, somehow
        pass




def chain():
    return Chain()


def process(command, env=None, clean_env=False, cwd=None, wait=False):
    p = Process(command)

    if wait:
        p.start()
        p.wait()


def run(command, env=None, cwd=None, clean_environ=False):
    pass
