with open("sonar-inputs.txt",'r') as input_data:
    lines = [int(x) for x in input_data.readlines()]

with open("sonar-inputs.txt","r") as f:
   text = f.read()

splitted = text.split('\n')

count = 0
last = None
our = []
for stak in splitted:
    if stak == "":
        continue
    num = int(stak)
    if last != None and num > last:
        count += 1
    last = num
print(count)
