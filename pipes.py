import os
import subprocess


class Process(object):
    def __init__(self, command):
        pass

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
            # wait=wait


def chain():
    return Chain()


def process():
    pass
