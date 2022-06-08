- 👋 Hi, I’m @BizCompliancer
- 👀 I’m interested in Business Compliance Automation
- 🌱 I’m currently learning Python, C++ and Business Compliacne in India
- 💞️ I’m looking to collaborate on Business Compliance Automation projects across the globe

<!---
BizCompliancer/BizCompliancer is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

### 1. Pexpect
Pexpect is a Python package for automating "test based" aka "command line" user facing applications. It works similar to linux expect. 
Pexpect allows your script to spawn a child application and control it as if a human were typing commands. It can be used for automating interactive applications such as ssh, ftp, passwd, telnet, etc. It can also be used to automate setup scripts for installing software package on different servers

#### Installation

    pip install pexpect

#### Usage
	https://www.geeksforgeeks.org/how-to-use-python-pexpect-to-automate-linux-commands/



>There are two important methods in Pexpect – expect() and send() (or sendline() which is like send() with a linefeed). 
> The expect() method waits for the child application to return a given string. The string you specify is a regular expression, so you can match complicated patterns. The send() method writes a string to the child application. From the child’s point of view it looks just like someone typed the text from a terminal. After each call to expect() the before and after properties will be set to the text printed by child application. The before property will contain all text up to the expected string pattern. The after string will contain the text that was matched by the expected pattern. The match property is set to the re match object.

*Note : Pexpect manual on shell script*
>Remember that Pexpect does NOT interpret shell meta characters such as redirect, pipe, or wild cards (>, |, or *). This is a common mistake. If you want to run a command and pipe it through another command then you must also start a shell.

#### Helpful Links

| Title | Link |
|-----|------|
|Documentation|https://pexpect.readthedocs.io/en/stable/index.html|
|Pexpect PyPi Repo|https://pypi.org/project/pexpect/|
|Github Repo|https://github.com/pexpect/pexpect|
|Video Link|https://www.youtube.com/watch?v=8QfD8V_-7ok|


### 2. Selenium
Selenium Python bindings provides a simple API to write functional tests using Selenium WebDriver. 
Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote , Safari etc.
#### Installation 

	pip install selenium

#### Usage
	https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test


#### Useful Resources
|title | Link |
|-------|--------|
| Documentation | https://www.geeksforgeeks.org/components-of-selenium/|
|github Repo | https://github.com/SeleniumHQ/selenium |
|Automation on Safari|https://geektechstuff.com/2019/05/07/web-scraping-introducing-selenium-python/|


#### Some useful links

* https://www.geeksforgeeks.org/selenium-python-tutorial/
* https://selenium-python.readthedocs.io/installation.html#introduction
* https://www.simplilearn.com/tutorials/python-tutorial/selenium-with-python

### 3. PyAutoGUI
PyAutoGUI is a Python module which can automate your GUI and programmatically control your keyboard and mouse. 
#### Installation
	pip3 install PyAutoGUI

#### Usage
	https://pyautogui.readthedocs.io/en/latest/#examples

#### Screenshot using pyautogui
First use below command to install `scrot` as it must be installed to use screenshot function in linux.
	sudo apt-get install scrot

Below links redirects to the example of screenshot using pyautogui.
	https://datatofish.com/screenshot-python/

#### Some useful links
* https://www.geeksforgeeks.org/message-boxes-using-pyautogui/
* https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/?ref=lbp
* https://pyautogui.readthedocs.io/en/latest/



### 4. Telethon

Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API as a users or through a bot account .

#### Installation
	pip3 install telethon




