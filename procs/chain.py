from __future__ import print_function
import os


class Chain(object):

    def __init__(self, processes):
        self.processes = processes


    def run(self):
        for proc, next_proc in zip(self.processes, self.processes[1:]):
            read, write = os.pipe()
            proc.set_stdout(write)
            next_proc.set_stdin(read)
        for proc in self.processes:
            proc.start()
        for proc in self.processes:
            proc.wait()
            if proc._stdout is not None:
                os.close(proc._stdout)


    @property
    def returncode(self):
        return self.processes[-1].returncode


    @property
    def stdout(self):
        return self.processes[-1].stdout

