import os

from procs import Process


TEST_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'test_data'
))


def test_chained_procs():
    ls = Process('ls')
    grep = Process('grep 2')
    chain = ls | grep
    chain.run()
    assert chain.returncode == 0
    assert chain.stdout == 'file2'

