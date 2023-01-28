YouTube Live Chat to Text File
by: Divinity
--------------------------------------------------------------------------
Description and Credits

This project reads YouTube live stream messages and stores them in 2
.txt files inside "outputs/name-message/" or "outputs/message-only/"
The first contains all the messages, and the latter contains all the
messages and the author's names.
FORMAT: <author>:   <message> or <message> (Oldest to Latest)

  
-Credits to:
Chat Downloader: https://github.com/xenova/chat-downloader
  (Library needed for this to work)
  
Codeium: https://www.codeium.com/
  (Codeium made this way easier to code)
--------------------------------------------------------------------------
How to run:

There's 2 ways to run this script:
you can run it through the .bat file, which is more
convenient or you can run it through your own Python IDE
which is better for when you want to add it to a larger project

Steps. Instructions
Installation:

.Bat Method:
1. Replace PATH in run_main.bat with the path to your Python.exe
2. Open cmd on this folder and run "pip install chat_downloader"
3. Run run_main.bat

IDE Method:
1. Load main.py on your Python IDE
2. Install chat_downloader from Pip
3. Run it inside the IDE

Use:
After the script starts running just paste the URL to the livestream
and let the program run. It'll automatically download each message
into their respective .txt files, updating every few seconds.

All of the outputs from this program are stored on the "outputs" folder
under the name <type>+<YouTube Watch ID>+<Random 6 digit number>.

So as a tip, if you wanna find a file from a specific livestream
copy the livestream's watch ID and search for it with that.

To quit the program simply close or terminate it, don't worry as
the text file is already saved.
--------------------------------------------------------------------------
Also, this project is licensed under the MIT license so feel free
to use it on an AI chatbot or whatever you want.
Anyways thanks for reading.
-Divinity
