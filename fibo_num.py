#!/usr/bin/python3
f1 = 1;
f2 = 1;

fnumber_cnt = 2;

fnumber_limit = int(input("fibonacci number? "));
print(f1, " ", f2, " ", end = '');

while(fnumber_cnt < fnumber_limit):
	temp = f1 + f2;
	print(temp, end = " ");
	f1 = f2;
	f2 = temp;
	fnumber_cnt += 1;
print();

print("N", fnumber_limit," = ", temp);
