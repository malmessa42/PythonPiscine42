from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# The name stands for "taqaddum" (تقدّم) — Arabic for "progress".

for elem in ft_tqdm(range(33300)):
    sleep(0.005)
print()
for elem in tqdm(range(33300)):
    sleep(0.005)
print()
