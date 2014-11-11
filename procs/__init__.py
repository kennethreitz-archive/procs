from .process import Process

def run(command):
    process = Process(command)
    process.run()
    return process
