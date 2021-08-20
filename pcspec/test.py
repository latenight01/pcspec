import sys , os


# avoid 'No module named...' error
sys.path.append(os.getcwd())
from pcspec import PC

p = PC()
print(p.json_info)