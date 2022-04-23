import sys
import os
from errors import *
if len(sys.argv) < 2:
  bindir = '/usr/local/bin'
else:
  if os.path.exists(sys.argv[1]):
    bindir = sys.argv[1]
  else:
    raise CannotInstallError('Path is not exists!')
if not os.getenv == 0:
  os.system(f'pkexec python3 {sys.argv[0]}')
  sys.exit()
else:
  for file in os.listdir('utils'):
    os.system(f'cp utils/{file} {bindir}/{file.split(".")[1]}')
  print(f'Done! HashUtils installed in {bindir} !')
