import os
import pandas as pd
import time

input = "digital-evolution-project-grades-1666330898.csv"
path = "../"
df = pd.read_csv(input)
urls = df.loc[:, ["student_repository_url"]].values.tolist()
assignment_name = df.loc[0, ["assignment_name"]].values.tolist()[0]
assignment_name = assignment_name.replace(" ", "")
print(assignment_name)
os.chdir("..")
directory = os.listdir()
if assignment_name not in directory:
    os.system(f"mkdir {path}{assignment_name}")
os.chdir(f"{assignment_name}")
os.system("pwd")
directory = os.listdir()
print(directory)
for url in urls:
    if url[0][29:] not in directory:
        print(url[0][29:])
        url = url[0]
        os.system(f"echo 'Working on {url}'")
        os.system(f"git clone --recurse-submodules {url};")
        time.sleep(5)