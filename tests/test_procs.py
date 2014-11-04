import os

from procs import Process


TEST_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'test_data'
))


def test_single_proc():
    ls = Process('ls {test_dir}'.format(test_dir=TEST_DIR))
    ls.run()
    assert ls.returncode == 0
    assert ls.stdout == u'file1\nfile2\nfile3\n'


def test_empty_output():
    cat = Process('cat /dev/null')
    cat.run()
    assert cat.stdout == u''


def test_returncode():
    assert not os.path.exists('/bin/nosuchcommand')

    p = Process('/bin/nosuchcommand')
    p.run()
    assert p.returncode == 127

