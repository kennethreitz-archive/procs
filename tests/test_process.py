import os

from procs import Process


TEST_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'test_data'
))

def tests_repr():
    p = Process('foo')
    assert repr(p) == '<Process: foo>'


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


def test_ok_if_returncode_0():
    p = Process('ls')
    p.run()
    assert p.ok is True


def test_not_ok_if_returncode_not_0():
    assert not os.path.exists('/bin/nosuchcommand')
    p = Process('/bin/nosuchcommand')
    p.run()
    assert p.ok is False
