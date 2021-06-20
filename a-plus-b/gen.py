import random
import os


try:
    # Create target Directory
    os.mkdir("testcases")
except FileExistsError:
    pass
os.system("g++ code/sol.cpp -o sol.out")
UPPER = 2**31 - 1
LOWER = -2**31
for i in range(1, 21):
    fin = os.path.join("testcases", f"{i}.in")
    fout = os.path.join("testcases", f"{i}.out")
    a = random.randint(LOWER, UPPER)
    b = random.randint(LOWER, UPPER)
    if not LOWER <= a + b <= UPPER:
        print("YEAHHH")
    with open(fin, "w") as f:
        print(a, b, file=f)
    os.system(f"./sol.out < {fin} > {fout}")
os.system("rm sol.out")