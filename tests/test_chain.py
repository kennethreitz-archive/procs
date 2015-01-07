import os

from procs import Process


TEST_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'test_data'
))


def test_chained_procs():
    ls = Process('ls {test_dir}'.format(test_dir=TEST_DIR))
    grep = Process('grep 2')
    chain = ls | grep
    chain.run()
    assert chain.returncode == 0
    assert chain.stdout.strip() == 'file2'

def test_multi_chained_procs():
    ls = Process('ls {test_dir}'.format(test_dir=TEST_DIR))
    grep = Process('grep 2')
    wc = Process('wc -c')
    chain = ls | grep | wc
    chain.run()
    assert chain.returncode == 0
    assert chain.stdout.strip() == '6'

