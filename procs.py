from __future__ import print_function
import os
import subprocess


class Process(object):
    def __init__(self, command):
        self.command = command
        self.environ = {}
        self.cwd = None
        self._stdout = None
        self._returncode = None


    def set_command(self, command):
        # process popen chain, etc
        self.command = command

    def set_environ(self, environ, clean=False):
        self.environ = dict() if clean else dict(os.environ)
        self.environ.update(environ)

    def set_cwd(self, cwd):
        # expand, discover, etc.
        self.cwd = cwd

    @property
    def stdin(self):
        return 'stdin'

    @property
    def stdout(self):
        if self._stdout:
            return self._stdout
        return 'stdout'

    @property
    def stderr(self):
        return 'stderr'

    @property
    def returncode(self):
        if self._returncode is not None:
            return self._returncode

    def run(self):
        self._subprocess = subprocess.Popen(
            args=self.command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        self._returncode = self._subprocess.wait()
        self._stdout = self._subprocess.stdout.read().decode()



class Chain(object):

    def __init__(self):
        self.processes = []

    def process(self, command):
        p = Process(command)
        self.processes.append(p)

        return p

    def link(self, x, y):
        print('Linking {} to {}'.format(x, y))

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
