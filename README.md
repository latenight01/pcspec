# pcspec
A pythonic tool for getting PC main specifications like `CPU` and `GPU` model , `RAM` and disk free space.

## Installation
`python -m pip install -r requirements.txt`


## Usage
```python
from pcspec import PC

pc = PC()

print(pc.json_info)
```
Output :
```json
{
    "CPU": "AMD A9-9420 RADEON R5",
    "Free disk space": "18 GB",
    "GPU": "AMD Radeon(TM) R5 Graphics",
    "Platform": "Windows",
    "RAM": "7.5 GB"
}
```
