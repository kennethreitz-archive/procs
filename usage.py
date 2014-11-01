import procs

chain = procs.chain()

uptime = chain.process('uptime')
cowsay = chain.process('cowsay')

chain.link(uptime.stdout, cowsay.stdin)
chain.start(wait=True)

print cowsay.stdout


# ConnectedProcess
# ActiveProcess
# PassiveProcess
