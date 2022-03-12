echo "All data will be deleted, that include images, error logs and satellite data."
echo "Press to confirm (y/n) > "

read confirmation

if [ $confirmation = 'y' ]; then
	rm -rf OctaCSV.csv
	touch OctaCSV.csv
	mv images/README.txt .
	rm -rf images/
	mkdir images
	mv README.txt images/
	rm -rf error_log.txt
	touch error_log.txt
fi
