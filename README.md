# auto-mess-registration
>register to desired mess without forgetting

Works for `linux` not tested for `Windows`

###Installion(for Ubuntu)
    $sudo apt install python3-pip
    $sudo pip3 install -U selenium
    
Now, you need to install the following webdrivers for `Selenium`:
* [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.28/)
* [PhantomJS](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2)

#####Extract both the files and follow listed steps
    $sudo cp ~/Downloads/chromedriver /usr/bin/
    $sudo cp ~/Downloadds/name_of_phantomJS_folder_here/bin/phantomjs /usr/bin/
    $sudo chmod +x /usr/bin/phantomjs
    $sudo chmod +x /usr/bin/chromedriver
and its done.

You also need to have google-chrome installed to use chromedriver
[Click here](https://www.google.com/chrome/browser/desktop/index.html) to install google-chrome

#####Now you can run the code as
    $python3 register_me.py
and you would be registered to desired mess.

>######NOTE: Error handling part needs to be checked.
