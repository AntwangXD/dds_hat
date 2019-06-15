make
gzip -f ad9834.ko

sudo cp -f ad9834.ko.gz /lib/modules/`uname -r`/kernel/drivers/staging/iio/frequency
