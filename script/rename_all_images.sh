num=1
for i in *.jpg
do
    num=$(($num+1))
    mv $i "lp_$num.jpg"
done
