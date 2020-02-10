"""Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

def sort1(l):
    return l[0]

def sort2(k):
    return float(k[1])


if __name__ == '__main__':
    l2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1 = str(name),str(score)
        l2.append(l1)
    l3 = min(l2,key=sort2)
    l4= l2.copy()
    for i in range(0,len(l2)):
        if(l3[1]==l2[i][1]):
            l4.remove(l2[i])
    l5=min(l4,key=sort2)
    l6=[]
    k=0
    for k in range(0,len(l4)):
        if(l5[1]==l4[k][1]):
            l6.append(l4[k])
    l6.sort(key=sort1)
    for z in l6:
        print(z[0])
