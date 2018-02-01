for i in {0..9180..540}
do
	echo "block " + $i
	python meh.py $i $(($i+540))
done
