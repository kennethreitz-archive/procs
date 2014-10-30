import pipes

chain = pipes.chain()

uptime = chain.process('uptime')
cowsay = chain.process('cowsay')

chain.link(uptime.std_out, cowsay.std_in)
chain.start(wait=True)

print cowsay.std_out


# ConnectedProcess
# ActiveProcess
# PassiveProcess