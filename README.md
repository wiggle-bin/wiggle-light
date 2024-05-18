# WiggleLight

## Prepare Raspberry PI

In `/boot/firmware/config.txt` add the following:

```
dtparam=spi=on
enable_uart=1
```

Reboot the Raspberry Pi via terminal

```
sudo reboot
```

## Use WiggleLight CLI

```
wiggle-light -h
```

## Installation for development

Updating packages on Raspberry Pi
```
pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
apt-get install libjpeg-dev zlib1g-dev
```

Installing package
```
sudo pip3 install -e .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```