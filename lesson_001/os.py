import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os.txt', 'w') as ff:
    ff.write(info)
o = 1222122121 + 444445454
print(o)