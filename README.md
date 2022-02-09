# NITK Captive Portal Auto Login

A python script that will automate the boring task of login to the captive portal again and again.

## Installation

Clone the repo and open the files using vscode. Then run the following commands from the terminal 

```bash
pip install selenium
pip install pyinstaller
```
Download driver for chrome from [here](https://sites.google.com/chromium.org/driver/downloads)

Extract the driver in c drive and add the link to path.

## Edit Config
Edit the config file with your login details

```python
username = "username_here"  // write your username here
pass_word = "password_here" // write your password here
```

## Make an exe
Run the following command from the terminal
```bash
pyinstaller --onefile -w auto_login.py
```
Inside the dist folder, you'll get your auto_login.exe file.

## Add shortcut to startup folder
Press Windows Key + R and open
```bash 
shell:startup
```
Copy the auto_login.exe file and paste it as a shortcut into Startup folder.

AND ENJOY!!



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)