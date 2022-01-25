import os

os.system("rm -rf /model/result")

with open('/model/run.sh', 'w') as f:
    f.write("python3 /model/codes/main.py --exp_dir /model/experiments_BD/EGVSR/001 --mode test --model /model/pretrained_models/EGVSR_iter420000.pth --opt test.yml --gpu_id 0\n")
    f.write("chmod -R 0777 /model/result\n")

os.system("chmod +x /model/run.sh")
os.system("/model/run.sh")

