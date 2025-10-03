#!/usr/bin/python

"""Given a dictionary with a values list, extract the key whose value has the most unique
values.
Input: test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
Output:"Best"
Explanation:3 (max) unique elements, 9,6,5 of "Best"""

def KeyWithUniqueValue(**x):
    unique_value=-1
    key_with_uniq_val=None
    for k,v in x.items():
        unique_count=len(set(v))
        if unique_count>unique_value:
            unique_value=unique_count
            key_with_uniq_val=k
            
    return key_with_uniq_val

test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}

result=KeyWithUniqueValue(**test_dict)
print(f'The key with unique value is: {result}')