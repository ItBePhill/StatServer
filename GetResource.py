import psutil
import subprocess as sp
class CPU():
    @classmethod
    def Get_CPU_Usage(self):
        cpu = psutil.cpu_percent(percpu=True, interval=0.1)
        print(f"CPU Usage: {cpu}")
        return cpu

class RAM():
    @classmethod
    def Get_RAM_Usage(self):
        ramp = psutil.virtual_memory()[2]
        print(f"RAM Usage: {ramp}%")
        return ramp
    @classmethod
    def Get_Available_RAM(self):
        rama = psutil.virtual_memory()[1]
        if str(rama/1000000000).split('.')[0] == "0":
            print(f"Available RAM: {round(rama/1000000, 2)} MB")
            return round(rama/1000000, 2)
        else:
            print(f"Availabl RAM: {round(rama/1000000000, 2)} GB")
            return round(rama/1000000000, 2)
    @classmethod
    def Get_Used_RAM(self):
        ramu = psutil.virtual_memory()[3]
        print(f"Used RAM: {round(ramu/1000000000, 2)} GB")
        return round(ramu/1000000000, 2)
    @classmethod
    def Get_Total_RAM(self):
        ramt = psutil.virtual_memory()[0]
        print(f"Total RAM: {round(ramt/1000000000, 2)} GB")
        return round(ramt/1000000000, 2)


class GPU():
    # raw strings avoid unicode encoding errors
    gpu_mem_cmd = r'(((Get-Counter "\GPU Process Memory(*)\Local Usage").CounterSamples | where CookedValue).CookedValue | measure -sum).sum'
    gpu_usage_cmd = r'(((Get-Counter "\GPU Engine(*engtype_3D)\Utilization Percentage").CounterSamples | where CookedValue).CookedValue | measure -sum).sum'
    @classmethod
    def run_command(self, command):
        val = sp.run(['powershell', '-Command', command], capture_output=True).stdout.decode("ascii")

        return float(val.strip().replace(',', '.'))
    @classmethod
    def Get_GPU_Mem(self):
        print(f"GPU Memory Usage: {round(self.run_command(self.gpu_mem_cmd)/1e6,1):<6} MB")
        return round(self.run_command(self.gpu_mem_cmd)/1e6,1)
        
    @classmethod
    def Get_GPU_Usage(self):
        print(f"GPU Load :        {round(self.run_command(self.gpu_usage_cmd),2):<6} %")
        return round(self.run_command(self.gpu_usage_cmd),2)
    

