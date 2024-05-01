
import time, shlex, subprocess
port = "127.0.0.1:8001"

while True: 
    cmd = "top -n1 | grep id, | awk '{print $8}'"
    output = subprocess.check_output(cmd, shell=True, text=True).rstrip().replace(",", ".")
    curr_util = round(100 - float(output), 1)
    cmd= f'curl -X POST http://{port}/ -d "curr_util={curr_util}%"'
    args = shlex.split(cmd)
    run = subprocess.run(args)
    print(f'Current CPU utilization: {curr_util}%')
    time.sleep(10)      
