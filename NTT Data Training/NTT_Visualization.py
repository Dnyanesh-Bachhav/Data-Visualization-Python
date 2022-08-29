# Data Visualization for students register in NTT Data Training program in DYP Akurdi...
# It visualiza data by bar charts...
import pandas as pd
import matplotlib.pyplot as plt
file = 'DYPatil Akurdi _NTT data Training registration.xlsx'
data = pd.read_excel(file)["Branch"]
branches = list(set(data))
student_count = []
AIDS = 0
IT = 0
ENTC = 0
Computer = 0
print(list(branches))
for branch in data:
    if branch == branches[0]:
        AIDS += 1
    elif branch == branches[1]:
        IT += 1
    elif branch == branches[2]:
        ENTC += 1
    elif branch == branches[3]:
        Computer += 1

student_count.extend([AIDS, IT, ENTC, Computer])
fig = plt.figure(figsize=(10, 5))
plt.bar(branches, student_count, color="green", width=0.4)
print(student_count)
plt.xlabel("Branches")
plt.ylabel("No. of Students")
plt.title("NTT Data Training Registrations")
plt.show()