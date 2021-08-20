# pcspec
A pythonic tool for getting PC main specifications like `CPU` and `GPU` model , `RAM` and disk free space.

## Installation
<small>Soon (via `pip`) ...</small>
<br>
`python -m pip install -r requirements.txt`


## Usage
```python
from pcspec import PC

pc = PC()

print(p.json_info)
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
### Features
- Supporting get the both AMD and Nvidia GPU infos

---

### __Note__ : I have not test this tool on many different machines and it can be buggy and unstable. so feel free to create any issue or PR