# autoKenpos

autoKenpos supports pepup.

## Preparation
1. Install FireFox
2. Download geckodriver which supports your FireFox
3. Install geckodriver
```bash
$ sudo cp geckodriver /usr/local/bin
$ chmod 755 /usr/local/bin/geckodriver
```

## Usage
```bash
$ sudo apt-get install xvfb
$ pip3 install -r requirements.txt
$ cd app
$ vim config/config.ini // Set up to fit your account
$ python3 autoKenpos.py
```

## Todo
1. Set up Docker container environment