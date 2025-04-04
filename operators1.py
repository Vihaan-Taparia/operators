#Finding average height of 5 trees



t1=98
t2=94
t3=41
t4=95
t5=11

sum=t1+t2+t3+t4+t5

avg=sum/5
print("The average height of the trees are:",avg)



#activity 2
amount=int(input("Please enter the ammount of money you want to withdraw:"))

note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
note_4=(((amount%100)%50)%10)%5
note_5=((((amount%100)%50)%10)%5)//1


print("Number of 100 rupees notes:",note_1)
print("Number of 50 rupees notes:",note_2)
print("Number of 10 rupees notes:",note_3)
print("Number of 5 rupee coins",note_4)
print("Number of 1 rupee coin:",note_5)


#activity 3...percentage

print("Enter marks obtained by student in 3 subject")
science = int(input("science:"))
math = int(input("math:"))
sst = int(input("sst:"))

sum=science+math+sst
perc=(sum/300)*100

print("The percentage of marks obtained by student is:",perc)