# def pangram():
#     s="We promptly judged antique ivory buckles for the next prize"
#     d=set(s.lower())-set(' ')
#     if len(d)==26:
#         print( "pangram")
#     else:
#         print("not pangram")
# pangram()

# a=int(input("enter a number "))
# b=int(input("enter a number "))
# c=int(input("enter a number "))
# d=int(input("enter a number "))
# k=a**b
# p=c**d
# print(k+p)


# n = int(input("enter a number "))
# p = int(input("enter a number "))
# print (p//2)



# def maximum(scores):
#     mini=maxi=0
#     mini1=max1=scores[0]
#     for i in range(1,len(scores)):
#         # if mini1=max1=scores[0]:
#         if mini1<scores[i]:
#             mini1=scores[i]
#             mini+=1
#         elif max1 > scores[i]:
#             max1=scores[i]
#             maxi+=1
#     return mini,maxi
# maximum(scores=)

# dic1={{1:10, 2:20},
# {3:30, 4:40},
# {5:50,6:60}}
# dic4 = {}
# for d in (dic1): 
#     dic4.update(d)
# print(dic4)

# dic4.update(dic1)
# dic4.update((dic2))
# dic4.update(dic3)
# print(dic4)

# dic2={1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 
# from collections import Counter
# Counter=0
# for value in dic2:
#     if value in dic1:
#         if value in dic3:
#             dic2[value] = dic1[value] + dic2[value]+dic3[value]

#     else:
#         pass 
# Cdict = Counter(dic3) + Counter(dic2) +Counter(dic1)
# print(dic2)       


# a=[1,-8,7,-9,-6]
# i=0
# c=[]
# while i<len(a):
#     n=a[i]
#     if n>0:
#         c.append(n)
#     else:
#         c.append(-n*0)
#     i=i+1
# print(c)        

# num=int(input("enter a number :"))
# a=num%10
# if a>0:
#     print(a)

# num=input("enter a name :")
# a=["pooja ","arti","priya"]
# i=0
# while i<len(a):
#     n=a[i]
#     print(i,n)
#     i=i+1

# i=0
# while i<10:
#     # i=i+1
#     if i==6 or i==3:
#         pass
#     else:
#         print(i)
#     i=i+1

# i=0
# while i <10:
#     i=i+1
#     if i==3 or i==4:
#         continue
#     print(i)
    
# i=0
# while i<10:
#     # i=i+1
#     if i==6 or i==3:
#         break
#     else:
#         print(i)
#     i=i+1


# def maximum(a,b):
#     if b==1:
#         return a
#     else:
#         return a*maximum(a,b-1)
# print(maximum(6,4))


# number=[60,59,45,23,90]
# largest=0
# secondlarg=0
# for i in range(len(number)):
#     if number [i]>largest:
#         largest=number[i]
#     elif number[i]<largest and  number[i]>secondlarg:
#         secondlarg=number[i]
# print(largest,secondlarg)


# import json
# a={"name":9,"class":0}
# with open("file.json","w") as f:
#     json.dump(a,f,indent=6)


# a={"m":90,"e":89}
# b=input("enter a subject: ")
# i=0
# while i<len(a):
#     n=a[i]
#     if b in n:
#         print(a[i][b])
#     i=i+1
# b={}
# for i in a:
# b=a.update({"n":9})
# print(a)

# my_file=open("people1-exercise.txt","w")
# my_file.write("rishabh - meerut \n imtiyaz - delhi \n nilima - cochin \n rati - shimla \n ayishah - delhi \n raghu - shimla \n naseer - kanpur \n karthikeyan - delhi \n salma - jaipur\n pankaj - delhi \n brijesh - delhi \n govind - delhi \n puneet - shimla \n siddhi - delhi \n suman - jaipur \n rajeev - shimla \n mohinder - delhi \n rajendra - jaipur \n priyanka - shimla \n neela - delhi \n sashi - jaipur")

# my_file.close()

# my_file=open("people1-exercise.txt","r")
# c=0
# for i in my_file:
#     c=c+1
# print(c)
# my_file.close()

    # © 2021 GitHub, Inc.


# a={{"a":20,"b":30},{"b":20,"c":40}}
# p={}
# for key ,value in a.items():
      
#     if value and 'b' in value.keys():
#         p.update(a)
#         sum += value['b'] 
  
# print(p)

# res = dict()
# for sub in a.values():
#     for key, ele in sub.items():
#         res[key] = ele + res.get(key, 0)
# print("The summation dictionary is : " + str(res)) 


# largest = list1[0] 
# lowest = list1[0] 
# largest2 = None
# lowest2 = None
# for i in list1[1:]:     
#     if i > largest: 
#         largest2 = largest
#         largest = i
#     elif largest2 == None or largest2 < i: 
#         largest2 = i
#     if i < lowest: 
#         lowest2 = lowest
#         lowest = i 
#     elif lowest2 == None or lowest2 > i: 
#         lowest2 = i 
              
# print("Largest element is:", largest) 
# print("Smallest element is:", lowest) 
# print("Second Largest element is:", largest2) 
# print("Second Smallest element is:", lowest2) 
  

vcount = 0;  
# ccount = 0;  
str = input("enter a name: ")
       
    #Converting entire string to lower case to reduce the comparisons  
str = str.lower();  
for i in range(0,len(str)):   

    if str[i] in ('a',"e","i","o","u","t"): 
        print(str[i],"vowal") 
        # vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        # ccount = ccount + 1;
        print(str[i],"constant")