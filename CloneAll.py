import os
import pandas as pd

input = "cellular-automata-assignment-grades-1664435504.csv"
df = pd.read_csv(input)
urls = df.loc[:, ["student_repository_url"]].values.tolist()
assignment_name = df.loc[0, ["assignment_name"]].values.tolist()[0]
assignment_name = assignment_name.replace(" ", "")
print(assignment_name)
os.system(f"mkdir ../{assignment_name}")
os.chdir(f"../{assignment_name}")
os.system("pwd")
print(assignment_name)
for url in urls:
    url = url[0]
    os.system(f"echo 'Working on {url}'")
    os.system(f"git clone {url};")