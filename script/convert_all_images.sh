for i in *.JPG
do
    filename=${i%%.*};
    convert $i "$filename.jpg"
done
