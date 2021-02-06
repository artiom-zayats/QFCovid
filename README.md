# QFCovid

A script to detect if there are covide vaccines available at any nearby QFC/FredMeyer locations.

This was written because my family got tired of checking every location manually. This script is
unpolished and buggy, but can typically get the job done.

*Warning: Use at your on risk. No compatability with any site's terms of service has been verified*

## Before your first run

This script using Selinium Web Driver.

1) Download the driver for your browser of choice. I chose [Chrome](https://chromedriver.chromium.org/downloads).
2) Put the driver in your executable path. I'm on Linux, so:

```shell
unzip chromedriver_linux64.zip 
mv chromedriver /usr/bin/
```
3) If you are using Chrome, you will probably need to bypass bot detection.

```shell
sudo perl -pi -e 's/cdc_/dog_/g' /usr/bin/chromedriver
```

## Running the script

```shell
python3 covid.py 
```

*Note: I'm sure there are dependencies that need to be installed, but this was for my personal use and just to get the code out there, so figure it out and submit a patch*

*Note: QFC's site is sensitive to what is visible on the screen in some instances, so there are a lot of sleeps. Also, depending on the resolution of the monitor of the machine that this is running on, you might need to make the browser window larger.*
