#QUESTION 2

#we use the file pig_weights.txt file for this question

#So the first thing is to sort the data according to each column and store output in 4 different file: 
#we need to align the columns first

#once the columns are aligned we will give the command : (aligned file: pig_weights_a.txt)
#FOR COLUMN ONE: "sort -k 1 -n pig_weights_a.txt > column1.txt
#OUTPUT: By "cat column1.txt" : Feed 1	Feed 2	Feed 3	Feed 4
#				57.1	67.7	102.2	84.7
#				58.7	66.3	97.5	85.8
#				60.8	68.3	102.6	87.9
#				61.8	69.9	98.9	90.3
#				65	74	100.5	83.2
# // we can see here that the column one is sorted and the rest of the columns are not.

#FOR COLUMN TWO: "sort -k 2 -n pig_weights_a.txt > column2.txt
#OUTPUT: By "cat column2.txt" : Feed 1	Feed 2	Feed 3	Feed 4
#				58.7	66.3	97.5	85.8
#				57.1	67.7	102.2	84.7
#				60.8	68.3	102.6	87.9
#				61.8	69.9	98.9	90.3
#				65	74	100.5	83.2

#FOR COLUMN THREE: sort -k 3 -n pig_weights_a.txt > column3.txt
#OUTPUT: By "cat column3.txt" : Feed 1	Feed 2	Feed 3	Feed 4
#				58.7	66.3	97.5	85.8
#				61.8	69.9	98.9	90.3
#				65	74	100.5	83.2
#				57.1	67.7	102.2	84.7
#				60.8	68.3	102.6	87.9

#FOR COLUMN FOUR: sort -k 4 -n pig_weights_a.txt > column4.txt
#OUTPUT: By "cat column4.txt" : Feed 1	Feed 2	Feed 3	Feed 4
#				65	74	100.5	83.2
#				57.1	67.7	102.2	84.7
#				58.7	66.3	97.5	85.8
#				60.8	68.3	102.6	87.9
#				61.8	69.9	98.9	90.3

#Hence now all the four columns have been sorted and saved separately in four different files.
