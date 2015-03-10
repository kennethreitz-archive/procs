from __future__ import print_function


class Chain(object):

    def __init__(self, processes):
        self.processes = processes

    def run(self):
        for i, proc in enumerate(self.processes, start=1):
            if i > 1:
                proc.set_stdin(self.processes[i-2].subprocess.stdout)
            proc.start()
            if i != len(self.processes):
                proc.wait(unread=True)
            else:
                proc.wait()

    @property
    def returncode(self):
        return self.processes[-1].returncode

    @property
    def stdout(self):
        return self.processes[-1].stdout

    def __or__(self, other):
        return Chain(self.processes + [other])
