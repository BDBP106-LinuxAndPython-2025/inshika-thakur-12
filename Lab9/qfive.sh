#!/bin/bash

echo "My name is $1"
echo "I am in $2 course"

var1=$(who ; echo $?)
echo "The output is:" $var1
var2=$(date ; echo $0)
echo "The second output is:" $var2
var3=$(uname ; echo $#)
echo "The third output is:" $var3
var4=$(date ; echo $@)
echo "The fourth output is:" $var4

