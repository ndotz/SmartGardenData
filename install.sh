echo '00 * * * * /usr/bin/python /mnt/sda1/sendSensorMessage.py
15 * * * * /usr/bin/python /mnt/sda1/sendSensorMessage.py
30 * * * * /usr/bin/python /mnt/sda1/sendSensorMessage.py
45 * * * * /usr/bin/python /mnt/sda1/sendSensorMessage.py' > task.txt
crontab task.txt
rm task.txt
opkg update
opkg install python-openssl
python login.py $1 $2
