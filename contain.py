from mininet.net import Mininet
from mininet.net import Containernet, OVSKernelSwitch
from mininet.node import Controller
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

setLogLevel('info')

#create network
net = Containernet(controller=RemoteController, switch=OVSKernelSwitch)

#create controller
info("adding controller\n")
c1 = net.addController('c1', Controller=RemoteController,port=6655,ip='127.0.0.1')
c2 = net.addController('c2', Controller=RemoteController,port=6633)

#create hosts
info('adding containers\n')
host1 = net.addDocker('host1', ip='192.168.2.10',dimage="ubuntu:trusty",mac='00:00:00:00:00:01')
host2 = net.addDocker('host2', ip='192.168.2.20',dimage="ubuntu:trusty",mac='00:00:00:00:00:02')
host3 = net.addDocker('host3', ip='192.168.2.30',dimage="ubuntu:trusty",mac='00:00:00:00:00:03')
host4 = net.addDocker('host4', ip='192.168.2.40',dimage="ubuntu:trusty",mac='00:00:00:00:00:04')

#create our switch
info('adding switch\n')
s1 = net.addSwitch('s1')

#link up our network
info('create links')
net.addLink(c2,s1)
net.addLink(s1,host1)
net.addLink(s1,host2)
net.addLink(s1,host3)
net.addLink(s1,host4)

#start network
info('starting network')
s1.start([c1,c2])
net.start()
#net.ping([host2,host3])
#start CLI
CLI(net)

#stop our network
info('shutting down network')
net.stop()
