#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class TwoSwitchesTopo(Topo):
    """Dois switches interconectados com
    metade dos hosts em cada um."""
    def build(self, n=2):
        switch_1 = self.addSwitch('s1')
        switch_2 = self.addSwitch('s2')
        self.addLink(switch_1, switch_2)
        for h in range(n):
            if h < n//2:
                host = self.addHost('h%s' %(h+1))
                self.addLink(host, switch_1)
            else:
                host = self.addHost('h%s' %(h+1))
                self.addLink(host, switch_2)


def createNetwork():
    qtd_hosts = int(input("Type the number of hosts: "))
    topo = TwoSwitchesTopo(n=qtd_hosts)
    net = Mininet(topo)

    return net


def startNetwork(net):
    net.start()


def testNetwork(net):
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Dumping switches connections")
    dumpNodeConnections(net.switches)
    print("Testing network connectivity")
    net.pingAll()


def stopNetwork(net):    
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')

    net = createNetwork()

    startNetwork(net)
    testNetwork(net)
    stopNetwork(net)

    net.stop()

