import configparser
config = configparser.ConfigParser()
config.sections()

config.read('example.ini')
config.sections()
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
for key in config['bitbucket.org']:
  print(key)
