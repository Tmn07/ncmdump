#!/bin/bash

#name=$1
#age=$2
#echo "name is ${name} & age is ${age}"
#
#echo $#


workdir=$(cd $(dirname $0); pwd)

#echo $workdir
#echo $(pwd)
#echo $workdir/main.py

COUNT=0
while  [ $# -gt 0 ]
do
    echo $1
    echo "python $workdir/main.py '$1'"
    python $workdir/main.py $1
    #　左移一个参数，这样可以使用$1遍历所有参数
    shift
    let COUNT=COUNT+1
done

read -p "Press [Enter] key to resume."