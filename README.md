# auto-mess-registration
>register to desired mess without forgetting

Works for `linux` not tested for `Windows`

### Installion(for Ubuntu)

    $sudo apt install python-pip
    $sudo pip3 install -U selenium
   
Now, you need to install the following webdrivers for `Selenium`:
* [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.28/)
* [PhantomJS](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2)

##### Extract both the files and follow listed steps

    $sudo cp ~/Downloads/chromedriver /usr/bin/
    $sudo cp ~/Downloadds/name_of_phantomJS_folder_here/bin/phantomjs /usr/bin/
    $sudo chmod +x /usr/bin/phantomjs
    $sudo chmod +x /usr/bin/chromedriver

and its done.

You also need to have google-chrome installed to use chromedriver
[Click here](https://www.google.com/chrome/browser/desktop/index.html) to install google-chrome

##### Now you can run the code as
 
    $python register_me.py    
 
and you would be registered to desired mess.

#### Adding to startup applications
        
    $mkdir ~/.auto-mess-reg/
    $mv path_to_register_me.py ~/.auto-mess-reg/

Press Windows(or Super) button on keyboard and search for startup applications, click add and fill in details as shown in image below:

[![Screenshot from 2017-04-11 01-15-44.png](https://s9.postimg.org/8m5gbob1r/Screenshot_from_2017-04-11_01-15-44.png)](https://postimg.org/image/52jilv8bv/)

You may not add it to startup application but if you add it you never need to worry about mess registration again.
##### Just make sure that if you add it to startup do_not_disturb flag is set to `True` in line 70 in the code.
>###### NOTE: Error handling part needs to be checked.
