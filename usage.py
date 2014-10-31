import pipes

chain = pipes.chain()

uptime = chain.process('uptime')
cowsay = chain.process('cowsay')

chain.link(uptime.stdout, cowsay.stdin)
chain.start(wait=True)

print cowsay.stdout


# ConnectedProcess
# ActiveProcess
# PassiveProcess
