from __future__ import print_function
import os
import subprocess


class Process(object):
    def __init__(self, command):
        self.command = command
        self.environ = {}
        self.cwd = None
        self._stdin = None
        self._stdout = None
        self._stdout_text = None
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


    def set_stdin(self, stdin):
        self._stdin = stdin

    def set_stdout(self, stdout):
        self._stdout = stdout

    @property
    def stdin(self):
        return 'stdin'

    @property
    def stdout(self):
        if self._stdout_text is not None:
            return self._stdout_text

    @property
    def stderr(self):
        return 'stderr'

    @property
    def returncode(self):
        if self._returncode is not None:
            return self._returncode

    @property
    def subprocess(self):
        if self._subprocess is not None:
            return self._subprocess

    def start(self):
        self._subprocess = subprocess.Popen(
            args=self.command,
            shell=True,
            stdin=self._stdin if self.stdin else subprocess.PIPE,
            stdout=self._sdout if self.stdout else subprocess.PIPE,
        )

    def wait(self):
        self._returncode = self._subprocess.wait()
        self._stdout_text = self._subprocess.stdout.read().decode()


    def run(self):
        self.start()
        self.wait()



    def __or__(self, other):
        return Chain([self, other])


class Chain(object):

    def __init__(self, processes=None):
        self.processes = processes if processes is not None else []


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

    def run(self):
        for proc, next_proc in zip(self.processes, self.processes[1:]):
            read, write = os.pipe()
            proc.set_stdout(write)
            next_proc.set_stdin(read)
        for proc in reversed(self.processes):
            print('starting', proc)
            proc.start()
        self.processes[-1].wait()


    @property
    def returncode(self):
        return self.processes[-1].returncode



def chain():
    return Chain()


def process(command, env=None, clean_env=False, cwd=None, wait=False):
    p = Process(command)

    if wait:
        p.start()
        p.wait()


def run(command, env=None, cwd=None, clean_environ=False):
    pass
