import time
import psutil

def generate_cpu_load(threshold):
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        print("Current CPU usage: {}%".format(cpu_percent))
        
        if cpu_percent > threshold:
            print("CPU load exceeded threshold! Generating alert...")
            
            break
        
        time.sleep(1)

if __name__ == "__main__":
    
    threshold = 90
    generate_cpu_load(threshold)
