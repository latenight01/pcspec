
import platform
import json
import psutil
from cpuinfo import get_cpu_info
import GPUtil
from GPUtil.GPUtil import GPU
# 
from pcspec.pyadl.pyadl import ADLManager, ADLDevice



class PC:
    def __init__(self) -> None:
        pass

    def disk_free_space(self, path):
        disk = psutil.disk_usage(path)
        amount_gb = disk.free // (1024**3)
        return f"{amount_gb} GB"

    @property
    def main_disk_free_space(self):
        return self.disk_free_space("/")

    @property
    def CPU(self) -> dict:
        CPU = get_cpu_info()
        del CPU["flags"]
        return CPU

    @property
    def CPU_name(self) -> str:
        value = self.CPU["brand_raw"]

        if "with" in value : 
            # some brand_raws are '[CPU_MODEL] with [GPU_MODEL]'
            # we just want [CPU_MODEL] part
            value = value.split("with")[0]

        return value


    @property
    def _nvidia_GPU(self) -> GPU:
        devices = GPUtil.GPUtil.getGPUs()
        if not devices :
            return None
        return devices[0]


    @property
    def _AMD_GPU(self) -> ADLDevice:
        devices = ADLManager.getInstance().getDevices()
        if not devices :
            return None
        return devices[0]

    @property
    def GPU_name(self):
        if self._nvidia_GPU is not None:
            return self._nvidia_GPU.name
        else:
            return self._AMD_GPU.adapterName.decode()

    @property
    def platform(self) -> str:
        """
        Returns the system/OS name, e.g. `Linux`, `Windows` or `Java`.
        """
        return platform.system()

    @property
    def RAM(self) -> str:
        amount = round(psutil.virtual_memory().total / (1024.0 ** 3), 1)
        return f"{amount} GB"

    @property
    def main_look_dict(self) -> dict:
        """
        a dict object including
        `platform`,`CPU`,`GPU`,`RAM`and `Free disk space`
        """
        data = {
            "Platform": self.platform,
            "CPU": self.CPU_name,
            "GPU": self.GPU_name,
            "RAM": self.RAM,
            "Free disk space": self.main_disk_free_space
        }
        return data

    @property
    def json_info(self) -> str:
        """
        a sorted easy readable `self.main_look_dict` with json format CLI string
        """
        return json.dumps(self.main_look_dict, indent=4, sort_keys=True)
    
    @property
    def string_info(self):
        """
        a sorted easy readable `self.main_look_dict` CLI 
        or tkinter text all-in-one string
        """
        value = f"Platform : {self.platform}\nCPU : {self.CPU_brand}\nGPU : {self.GPU_brand}\nRAM : {self.RAM}\nFree space : {self.main_disk_free_space}"
        return value

