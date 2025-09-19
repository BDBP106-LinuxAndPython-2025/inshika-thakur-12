#!/usr/bin/python

P=float(input("Enter principle: "))
ROI=float(input("Enter rate of interest in percentage pa: "))
Time=float(input("Time in years: "))
SI=(P*ROI*Time) / 100
Amount=P+SI
print(f'Simple Interest: {SI:f} ')
print(f'The total amount is: {Amount:f} ')


