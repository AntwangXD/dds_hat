clock/clock
chown -R alarm /sys/bus/iio/devices/iio\:device0/*
chgrp -R alarm /sys/bus/iio/devices/iio\:device0/*

chown -R alarm /sys/bus/iio/devices/iio\:device1/*
chgrp -R alarm /sys/bus/iio/devices/iio\:device1/*

echo 1 > /sys/bus/iio/devices/iio\:device1/out_altvoltage0_out_enable
echo 5000 > /sys/bus/iio/devices/iio\:device1/out_altvoltage0_frequency0


echo 4095 > /sys/bus/iio/devices/iio\:device0/out_voltage0_raw



