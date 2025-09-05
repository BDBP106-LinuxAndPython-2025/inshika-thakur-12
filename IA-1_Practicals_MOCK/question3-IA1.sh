#QUESTION THREE

#In order to sort the data according to the height column we will first use the command:
#COMMAND: " sort -t ',' -k 2 -g SOCR-HeightWeight.csv > heightsort.txt " (This will sort it and shift it to new files.)
#To check if it is sorted: cat heightsort.txt | tail -n15
#OUTPUT:1163,74.24899,150.2167
#	15967,74.25069,150.0567
#	8829,74.2727,144.66
#	4509,74.28376,147.7877
#	17080,74.2957,170.5479
#	10331,74.36328,164.6643
#	21950,74.42744,141.7416
#	16146,74.47517,130.9092
#	22472,74.51784,146.9867
#	24802,74.53177,148.9104
#	15210,74.59993,147.0372
#	13682,74.74047,155.5462
#	16753,74.8489,122.1664
#	2482,75.11519,153.9562
#	1894,75.1528,146.9701
#Hence here according to the sorted list 75.1528 is the height of tallest person

#Here in the sort command -t is the field separator, 2 is the column number and -g is the general sort command

#NOw to check if the tallest person weighs the most we first sort the weight column using the command:
#COMMAND: "sort -t ',' -k 3 -n SOCR-HeightWeight.csv > weightsort.txt"
#To check if the file has been sorted and stored in other file we use command: "cat weight.txt | tail -n15"
#OUTPUT:11975,71.26903,166.1956
#	5395,70.75604,166.2812
#	4625,71.78019,166.3016
#	11754,70.3846,166.7687
#	12884,71.58499,167.8045
#	368,72.32489,168.229
#	4344,73.52131,168.881
#	7997,69.57329,169.1268
#	17080,74.2957,170.5479
#	10235,70.71295,170.924
#Here it can be seen that the weight column is sorted numerical wise and the maximum weight is 170.924 pounds and the height of that person is 70.71295inches (not the tallest person)



