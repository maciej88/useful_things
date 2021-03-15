import os
import platform

#easy way: nodename, realase, version and machine
print(os.uname())

#some hardcore - direct infos:
my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Realase: {my_system.release}")
print(f"System Version: {my_system.version}")
#bonus :)
print(f"Processor: {my_system.processor}")
