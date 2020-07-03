Bandit game

IP: bandit.labs.overthewire.org:2220

Level 0 {
	bandit0:bandit0
}

Level 1 {
	bandit1:boJ9jbbUNNfktd78OOpsqOltutMc3MY1

	file - located at home directory,
	to acces the file I used:
		$ cat ./-
}

Level 2 {
	bandit2:CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

	file "spaces in file name" located at home directory,
	to read the file I used:
		$cat spaces\ in\ this\ filename 
}

Level 3 {
	bandit3:UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

	folder inhere located at home dir, inside there is a hidden file .hidden
	use cat to read it.
		$ cat inhere/.hidden
}

Level 4 {
	bandit4:pIwrPrtPN36QITSp3EQaw936yaFoFgAB

	folder inhere located at home directory, inside there are a bunch of files:
		./-file00 to ./-file09

	the only human-readable file is ./-file07
}

Level 5 {
	bandit5:koReBOKuIDDepwhWk7jZC0RTdopnAYKh

	file is located at the inhere folder,
	file details: human-readable, 1033 bytes in size, not executable

	to find it I used:
		$ find . -type f -readable ! -executable -size 1033c
}

Level 6 {
	bandit6:DXjZPULLxYr17uwoI01bNLQbtFemEgo7

	file is located somewhere on the server and has the following properties:
		owned by user bandit7
		owned by group bandit6
		33 bytes in size

	to find it use the following command:
		$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null

	2>/dev/null only show the accesible files
}

Level 7 {
	bandit7:HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

	the password is located in the file data.txt next to the word "millionth"

	to find it I used the command:
		$ grep millionth data.txt
}

Level 8 {
	bandit8:cvX2JJa4CFALtqS87jk27qwqGhBM9plV

	password is stored in the file data.txt, and it only appears once

	find it using the following command:
		$ cat data.txt | sort | uniq -u
}

Level 9 {
	bandit9:UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

	password is stored in the file data.txt, in one of the few human readable files,
	preceded by several "=" characters

	find it using the following command:
		$ string data.txt | grep "="

	Info:
		strings - print the strings of printable characters in files.
}

Level 10 {
	bandit10:truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

	password is stored in the file data.txt and is encoded in base64

	encoded password: VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==

	to decoede the file use the following command:
		$ cat data.txt | base64 --decode

	this command outputs the following:
		The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
}

Level 11 {
	bandit11:IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

	the password is stored in the file data.txt where all lowercase and uppercase letters have been rotated 13 positions

	encoded file:
	Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh

	to decode the file use the following command:
		$ cat data.txt | tr [A-Za-z] [N-ZA-Mn-za-m]
		The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
}

Level 12 {
	bandit12:5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

	the password is on the data.txt file
	this file has been compressed several times and then hexdumped

	First step: reverse hexdump with xxd command
		$ xxd -r data.txt > data_xxd

	Second step: see type of file (compression)
		$ file data_xxd

		this will tell the type of compression used: gzip, bzip2m tar

	Third step: decompress the data
		This is different for every type of compression

		gzip:	$ zcat in_file > out_file
		bzip2:	$ bzip2 -d file
		tar:	$ tar xvf file

	Forth step: repeat steps 2 and 3 until done

	Finally we find the file decompressed:

		The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

}

Level 13 {
	bandit13:8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

	the password is stored on /etc/bandit_pass/bandit14 and can only be read by the user bandit14

	to acces we don't have the password, we have a private ssh key located on the main directory:
		sshkey.private > sshkey_bandit13.private

		so we just have to ssh into the user with the following command:
			$ ssh bandit14@localhost -i sshkey.private

		and now we are the user bandit14 and we just can go and read the file /etc/bandit_pass/bandit14
			$cat /etc/bandit_pass/bandit14
			4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
}

Level 14 {
	bandit14:4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

	The password for the next level can be retrieved by submiting the current password to localhost at port 30000

	This can be done using the nc command:
		$ nc [-options] hostname port[s] [ports] ...
	ie:
		$ nc localhost 30000

	And then send the current password:
		4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
}

Level 15 {
	bandit15:BfMYroe26WYalil77FoDi9qh59eK5xNr

	The password for the next level can be retrieved by submiting the current password to localhost at port 30001 using ssl encryption

	This can be done using the openssl command:
		$ openssl s_client -connect localhost:30001

	And send the current password:
		BfMYroe26WYalil77FoDi9qh59eK5xNr
}

Level 16 {
	bandit16:cluFn7wTiGryunymYOu4RcffSxQluehd

	The credentials for the next level can be found by submiting the current password to a port located from 31000-32000

	First we have to find out which of this ports speak ssl, the others will just return whatever it's send

	To find the open ports we use Nmap:

		$ nmap -v -sV -p 31000-32000 localhost

		Nmap outputs more lines but this are the important ones for this Level:

		PORT      STATE SERVICE     VERSION
		31046/tcp open  echo
		31518/tcp open  ssl/echo
		31691/tcp open  echo
		31790/tcp open  ssl/unknown
		31960/tcp open  echo


		This shows the open ports and the service
		So we can see that ssl is only on ports 31518 and 31790, but idk why it's 31790 that's the correct one
		Probably because all the other have echo so that means they just reply whatever is send?¿?¿?

		Anyway we connecto to that port on localhost
			$ openssl s_client -connect localhost:31790

		And send the current password: cluFn7wTiGryunymYOu4RcffSxQluehd

		Finally we get a private key for the next level:

		-----BEGIN RSA PRIVATE KEY-----
		MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
		imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
		Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
		DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
		JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
		x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
		KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
		J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
		d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
		YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
		vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
		+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
		8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
		SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
		HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
		SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
		R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
		Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
		R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
		L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
		blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
		YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
		77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
		dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
		vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
		-----END RSA PRIVATE KEY-----
}

Level 17 {
	bandit17:Uses private key (bandit17_sshkey.private )

	The password is the different line between two files: password.new and password.old

	Using the command diff:
		$ diff password.new password.old
		42c42
		< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
		---
		> w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii

	Getting the new password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
}

Level 18 {
	bandit18:kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

	The .bashrc has been modified to logout when you login with ssh

	But we can access using the flag -t on the ssh command:
		$ ssh -t -l bandit18 bandit.labs.overthewire.org -p 2220 /bin/sh

	This opens a shell with user bandit18.

	Then just get the password from the readme file on the main directory
}

Level 19 {
	bandit19:IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

	The password file is located on /etc/bandit_pass/ directory and is owned by usr: bandit20
	We'll need to do priv esc.

	To get acces to the next level we have to use the setuid binary in the homedirectory,
	first we can try to execute it without arguments:
		$ ./bandid20-do
		Run a command as another user.
		  Example: ./bandit20-do id

	So we just have to do as told:
		$ ./bandit20-do cat /etc/bandit_pass/bandit20
		GbKksEFF4yrVs6il55v6gwY5aVje5f0j
}

Level 20 {
	bandit20:GbKksEFF4yrVs6il55v6gwY5aVje5f0j

	So we have the ./suconnect program (setuid binary) that takes a local port as an argument
	and reads whatever the port recieve, if what recieves is the actual password then program sends the next password.

	First i used Nmap to see if there was any open ports, spolier alert, there weren't:
		PORT      STATE SERVICE VERSION
		22/tcp    open  ssh     OpenSSH 7.4p1 (protocol 2.0)
		113/tcp   open  ident
		30000/tcp open  ndmps?

	Then i tried using the note: connecting to my own network daemon
	I tried to look for daemons using:
		$ ps -ef
	I found some but i'm not sure what they were.

	So i decided tho ask for help on the discord server (thx BAD#7399)

	first of all we have to use tmux to have various terminals (one for netcat the other for the program)

	Terminal1:
	and i was on the wrong path with the daemons, i just have to create a service using netcat:
		$ nc -l -p 9600
	with this i'm creating a listener at localhost on port 9600 (chosen randomly i guess, from the closed ones)

	Terminal2:
	and then run the program on an other terminal
		$ ./suconnect 9600

	Terminal1:
	finally send the password on the first terminal

	And level finished
}

Level 21 {
	bandit21:gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

	A program is runing at regular intervals from cron, it's suggested to look at the /etc/cron.d/
	for the configuration and see what program is being executed.

	If we go and look at the suggested folder we see the folloing files:
		-rw-r--r--  1 root root   62 May 14 13:40 cronjob_bandit15_root
		-rw-r--r--  1 root root   62 May 14 14:03 cronjob_bandit17_root
		-rw-r--r--  1 root root  120 May  7 20:14 cronjob_bandit22
		-rw-r--r--  1 root root  122 May  7 20:14 cronjob_bandit23
		-rw-r--r--  1 root root  120 May 14 09:41 cronjob_bandit24
		-rw-r--r--  1 root root   62 May 14 14:04 cronjob_bandit25_root
		-rw-r--r--  1 root root  102 Oct  7  2017 .placeholder

	Next we look what the cronjob_bandit22 cronthingi does:
		@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
		* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

	This cronthingi at reboot executes the /usr/bin/cronjob_bandit22.sh and sends the outputs to /dev/null.

	And if we see what the bash script does;
		#!/bin/bash
		chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
		cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

	Changes the acces permissions of the /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv file, and outputs the next password to the same file

	Reading the file we get the next password:
		Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
}

Level 22 {
	bandit22:Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

	A program is runing at regular intervals from cron, it's suggested to look at the /etc/cron.d/
	for the configuration and see what program is being executed.

	looking at the /etc/corn.d/cronjob_bandit23 cronthingi:
		@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
		* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

	looking at the bash script:
		#!/bin/bash

		myname=$(whoami)
		mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

		echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

		cat /etc/bandit_pass/$myname > /tmp/$mytarget

	And doing this script using myname=bandit23 we get:
		mytarget=8ca319486bfbbc3663ea0fbe81326349

	Finally the password is the file /tmp/8ca319486bfbbc3663ea0fbe81326349
		jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

}

Level 23 {
	bandit23:jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

	A program is runing at regular intervals from cron, it is suggested to look at the /etc/cron.d/
	for the configuration and see what program is being executed.

	looking at the /etc/corn.d/cronjob_bandit23 cronthingi:
		@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
		* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null

	looking at the bash script:
		#!/bin/bash

		myname=$(whoami)

		cd /var/spool/$myname
		echo "Executing and deleting all scripts in /var/spool/$myname:"
		for i in * .*;
		do
			if [ "$i" != "." -a "$i" != ".." ];
			then
				echo "Handling $i"
				owner="$(stat --format "%U" ./$i)"
				if [ "${owner}" = "bandit23" ]; then
					timeout -s 9 60 ./$i
				fi
				rm -f ./$i
			fi
		done


	This script executes and then removes all scripts located on /var/spool/bandit24/

	We create a directory on /tmp/, named pleb to store all our stuff,
	and then create th script that gives us the next password:
		#!/bin/bash

		cat /etc/bandit_pass/bandit24 > /tmp/pleb/pass

	next we give access to everyone to the script and directory, 
		$ chmod -R 777 /tmp/pleb/

	finally copy the script to /var/spool/bandit24:
		$ cp /tmp/pleb/pleb.sh /var/spool/bandit24/

	just check the pass file to get the password:
	UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
}


Level 24 {
	bandit24:UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

	A daemon is listenint at port 30002 and will give the password for bandit25 if given the current password
	and a secret numeric 4 pin code:
		currentpass abcd

	with the bash script on file bandit24script.sh we can acomplish that:
		Correct!
		The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

}

Level 25 {
	bandit25:uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

	shell of user bandit26:
		bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
	found running:
		$ cat /etc/passwd | grep bandit26

	the file /usr/bin/showtext is: POSIX shell script, ASCII text executable
	contains {
		#!/bin/sh

		export TERM=linux

		more ~/text.txt
		exit 0
	}

	if we find a way to force the more command to not show the 100% of the file, we can use the interactive mode.
	if we squezze the terminal vertically we can acomplish that.

	now just by pressing v we'll enter the interactive mode, that is like if we opened the file with vim,

	when we are inside vim whe can open other files using :edit
		$ :edit /etc/bandit_pass/bandit26

	and we have the key

	Second way and better way, spawn a shell inside vim.
	Do the same as before until you open vim, then type the following commands:
		$ :set shell=/bin/bash
		$ :shell

	Now you have a shell
}

Level 26 {
	bandit26:5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

	if we do the same as the level before and get a shell, then we just have to execute te program on the main directory:
		bandit27-do
	the name is pretty explanatory by itself.

	and we get the password for the next level from /etc/bandit_pass
}

Level 27 {
	bandit27:3ba3118a22e93127a4ed485be72ef5ea

	For this level we have to clone the repository from repo, the password for bandit27-git is the same as bandit27

	First we make a folder on /tmp/ to have all our stuff, and clone the repo inside:
		$ mkdir /tmp/pleb
		$ cd /tmp/pleb
		$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo

	now we have the repo on /tmp/pleb and inside there is a README with the next password:
		The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
}

Level 28 {
	bandit28:0ef186ac70e04ea33b4c1853d2526fa2

	As the level before we clone the repo, BUT the README.md file has the password "blocked":
		# Bandit Notes
		Some notes for level29 of bandit.

		## credentials

		- username: bandit29
		- password: xxxxxxxxxx


	first we can see if there have been any changes on this repo with the  following command:
	NOTE: this command has to be used inside the repo!
		$ git log
			commit edd935d60906b33f0619605abd1689808ccdd5ee
			Author: Morla Porla <morla@overthewire.org>
			Date:   Thu May 7 20:14:49 2020 +0200

			    fix info leak

			commit c086d11a00c0648d095d04c089786efef5e01264
			Author: Morla Porla <morla@overthewire.org>
			Date:   Thu May 7 20:14:49 2020 +0200

			    add missing data

			commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
			Author: Ben Dover <noone@overthewire.org>
			Date:   Thu May 7 20:14:49 2020 +0200

			    initial commit of README.md

	As we can see the file has been changed due to an "info leak"
	we can see the difference between the two commits given their id:
		$ git diff edd935d60906b33f0619605abd1689808ccdd5ee c086d11a00c0648d095d04c089786efef5e01264

		diff --git a/README.md b/README.md
		index 3f7cee8..5c6457b 100644
		--- a/README.md
		+++ b/README.md
		@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
		 ## credentials
		 
		 - username: bandit29
		-- password: bbc96594b4e001778eee9975372716b2
		+- password: xxxxxxxxxx

	And we finally have the password for bandit29:
	 - username: bandit29
	-- password: bbc96594b4e001778eee9975372716b2
	+- password: xxxxxxxxxx
}

Level 29 {
	bandit29:bbc96594b4e001778eee9975372716b2
}

Level 30 {
	bandit30:5b90576bedb2cc04c86a9e924ce42faf
}