import subprocess
subprocess.call(['nosetests', '--tests', 'src/data/', 'src/models/', 'src/features/', 'src/visualization/'])

