# iPhone Copy to PC Shortcut Helper

Directly transfer your files, photos, video or any media to any PC or Linux wirelessly over the lan via iPhone's built-in Shortcuts application with Http Post request without any necessity of 3rd party drive/web/internet services. 
Also, two way **Clipboard** sync for text! 

**Important:** Note that this is only for private Home or Personal network on Wireless LAN. **Do not** use in production or on shared or public networks, as data is transmitted via HTTP and not encrypted. 

![Send2PC.png](media/Send2PC.png)

## ## Installation and Usage

### Step 1:
- Run / Compile & Run the script as detailed below 
  
  **OR**
  
- Download the pre-compiled executable from [Releases page](https://github.com/shajul/ShortcutsListener/releases/latest) for Windows.
  
### Step 2:
- **Install Shortcut** from [RoutineHub](https://routinehub.co/shortcut/17314/). Configure the shortcut with the ip address shown in the console on PC.

All selected files, photos and videos will be transfered to PC. Or you can use it from the share sheet.


## Notes

- Note: Transfer stops as soon as iPhone screen goes off. You need to keep the screen on while you are transfering too many photos or huge videos.
- Note: To make large amount of photo/video transfer 'Allow Sharing Large Amounts of Data' needs to be turned on from 'Settings -> Shortcuts -> Advanced' screen.
- Note: Files are sent to ~\Downloads by default. Specify `--download-dir <directory>` when running the host to set a new one. 
- Note: To run as a Windows service, configure with the tool [NSSM - the Non-Sucking Service Manager](http://nssm.cc/)

## Run / Compile & Run hints

- Create Virtual environment with `python -m venv .`
- Activate environment with `Scripts\activate.bat` on Windows or `. Scripts/activate` on Linux host.
- Install requirements with `pip install Flask requests pyperclip`
- Optional requirements for compiling to executable `pip install pyinstaller`
- Run with `python ShortcutsListener.py`
- Compile with `pyinstaller -c -i ShortcutsListener.ico -F .\ShortcutsListener.py` to get a single executable.
