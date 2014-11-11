import procs


def test_run_is_same_as_Process_run():
    process = procs.Process('ls')
    process.run()
    p = procs.run('ls')
    assert p.returncode == process.returncode
    assert p.stdout == process.stdout

