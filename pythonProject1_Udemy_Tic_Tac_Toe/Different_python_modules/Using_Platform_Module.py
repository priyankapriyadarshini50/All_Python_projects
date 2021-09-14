import platform
import os
print(platform.uname())
print(platform.platform())
print(platform.platform(aliased=1, terse=0))
print(platform.platform(aliased=4, terse=1))  # terse=1 or True, short output

# RETURNS THE NAME OF THE PROCESSOR
print(platform.machine())

# RETURNS THE FULL NAME OF PROCESSOR
print(platform.processor())

# RETURNS THE GENERIC OS NAME
print(platform.system())

# RETURNS THE VERSION OF THE OS
print(platform.version())

# RETURNS THE VERSION OF PYTHON
print(platform.python_version())
print(platform.python_version_tuple())

# RETURNS THE PYTHON IMPLEMENTATION IN STRING FORMAT
print(platform.python_implementation())

# RETURNS SYSTEM, NODE, RELEASE, VERSION, MACHINE
print(platform.uname())
# print(os.uname())

# RETURNS THE NODE(ADDRESS OF YOUR COMPUTER IN THE NETWORK)
print(platform.node())

# RETURNS THE OS RELEASE VERSION
print(platform.release())

# RETURN PYTHON VERSION IN FORM OF A TUPLE(3.9.5 -> (3,9,5))
print(platform.python_version_tuple())

