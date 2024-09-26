#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNetConnections
from mininet.log import setLogLevel
from mininet.clean import cleanup


class TwoSwitchesTopo(Topo):
    """Dois switches interconectados com
    metade dos hosts em cada um."""
    def build(self, n, perf_param):
        switch_1 = self.addSwitch('s1')
        switch_2 = self.addSwitch('s2')
        self.addLink(switch_1, switch_2)
        for h in range(n):
            if h < n//2:
                host = self.addHost('h%s' %(h+1))
                self.addLink(host, switch_1, **perf_param)
            else:
                host = self.addHost('h%s' %(h+1))
                self.addLink(host, switch_2, **perf_param)


def createNetwork():

    satellite_params = dict(bw=1000, 
                            delay='490ms',
                            loss=1,
                            max_queue_size=5000,
                            use_htb=True)

    qtd_hosts = int(input("Type the number of hosts: "))
    topo = TwoSwitchesTopo(qtd_hosts, satellite_params)
    net = Mininet(topo)

    return net


def startNetwork(net):
    net.start()


def testNetwork(net):
    print("Dumping connections:\n")
    dumpNetConnections(net)
    print("\nTesting network connectivity\n")
    net.pingAll()


def stopNetwork(net):    
    net.stop()


if __name__ == '__main__':
    cleanup()

    setLogLevel('info')

    net = createNetwork()

    startNetwork(net)
    testNetwork(net)
    stopNetwork(net)
