import sys , os
from pcspec import PC

# avoid 'No module named...' error
sys.path.append(os.getcwd())


p = PC()
print(p.json_info)