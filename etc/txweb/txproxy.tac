from twisted.application import internet, service
from twisted.web import static, server, vhost, script, proxy

# define proxy target
rproxy = proxy.ReverseProxyResource('localhost', 8088, '')

# create virtualhosting
root = vhost.NameVirtualHost()
# point vhosting as proxy target
root.default = rproxy
# create site with vhosting as root
site = server.Site(root)

application = service.Application('txcorn')
services = service.IServiceCollection(application)

server = internet.TCPServer(80, site)
server.setServiceParent(services)
