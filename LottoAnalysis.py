import random

reg_num = []
pb_num = []


#Since I don't have the pbnumbers.txt file, I wrote this function to generate a random one.
#654 lines, first 5 numbers are 1-69, the PB num is 1-26
def gen_file():
  with open("pbnumbers.txt", "w") as f:
    for n in range(0,654):
        for n in range(0,5):
            f.write(f"{random.randint(1,69)} ")
        f.write(f"{random.randint(1,26)}\n")

#This function will read each line in the file and break them up into lists we can query later
def read_file():
  with open("pbnumbers.txt", "r") as f:
    for line in f.readlines():
      nums = [int(x) for x in line.split()]
      reg_num.extend(nums[0:5])
      pb_num.append(nums[5])

def frequency(c_list, c_range): #Take in the curent list and current range
  possible_nums = list(c_range) #The possible numbers range is passed on below.
  frequency_dict = dict()
  counter = 0
  for n in possible_nums:
      frequency_dict[n] = c_list.count(n)
  return frequency_dict

def sort_by_freq(freq_dict):
  commonality = list()
  for k,f in freq_dict.items():
    commonality.append([f,k])
  return sorted(commonality)


def least_com():
  pass

def overdue():
  pass

def report(c_list,r_type):
  print(r_type)
  for n in range(1,11):
    print(f'{n}. {c_list[n-1][1]} was picked {c_list[n-1][0]} times')


pb_range = range(1,27)
reg_range = range(1,70)
gen_file()
read_file()
pbfrequency_dict = frequency(pb_num,pb_range)
regfrequency_dict = frequency(reg_num,reg_range)
pbCommonality = sort_by_freq(pbfrequency_dict)
regCommonality = sort_by_freq(regfrequency_dict)
pb_top_ten = pbCommonality[-10:]
regTopten = regCommonality[-10:]

report(sorted(pb_top_ten, reverse=True),"Top Ten PowerBall Numbers")
print("\n")
report(sorted(regTopten, reverse=True), "Top Ten Regular Numbers")

