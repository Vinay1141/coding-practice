v = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
vowels = ['a','e','i','o','u']
s = [1,2,3,4,5]
w = []
for i in range(len(s)):
    w.append(v[s[i]])
count =0
for i in range(len(w)):
    for j in range(len(w[i])):
        if  w[i][j] in vowels:
            count+=1
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] + s[j] == count:
            print(s[i],s[j])
            break
            

        
