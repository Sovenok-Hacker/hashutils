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
if not os.getuid() == 0 and not len(sys.argv) < 2:
  os.system(f'pkexec sh -c "cd {os.getcwd()} && python3 {sys.argv[0]} {sys.argv[1]}"')
  sys.exit()
elif not os.getuid() == 0 and len(sys.argv) < 2:
  os.system(f'pkexec sh -c "cd {os.getcwd()} && python3 {sys.argv[0]}"')
  sys.exit()
else:
  for file in os.listdir('utils'):
    print(f'Copying {file.split(".")[0].upper()} algorhytm binary!')
    os.system(f'cp utils/{file} {bindir}/{file.split(".")[0]}')
    print(f'CHMODing {file.split(".")[0].upper()} algorhytm binary!')
    os.system(f'chmod +x {bindir}/{file.split(".")[0]}')
  print(f'Done! HashUtils installed in {bindir} !')
