import os
import subprocess



class Process(object):
    def __init__(self, command):
        pass

    def start(self):
        pass

    @property
    def std_in(self):
        return 'std_in'

    @property
    def std_out(self):
        return 'std_out'

    @property
    def std_err(self):
        return 'std_err'


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