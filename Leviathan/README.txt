Host: leviathan.labs.overthewire.org:2223

Leviathan0 {
	leviathan0:leviathan0

	there is a hidden directory on the main folder named .backups, inside there is a file named bookmarks.html:
		bookmarks.html: HTML document, ASCII text, with very long lines

	if we search for leviathan inside the file we found this at line 1049:
		<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
}


Leviathan1 {
	There is a program called check on the user directory.
	Once executed it asks for a password, i read a hint online were it said that for the people that watched the movie Hackers it would be
	and easy task to get the password, or something similar to that. So i decided to search for the hacks that appeared on the movie.

	The first thing i found was about common passwords such as:
		1234
		123456
		password
		god
		sex
		...

	I typed some of this passwords and the correct one was sex.

	Then the program opened a sh shell as the user leviathan2, so to get the next password I just needed to go to the /etc/leviathan_pass/ directory.

	An other way to do this level is using the ltrace command:
	If we first use the file command with the executable:
		$ file check
		check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c735f6f3a3a94adcad8407cc0fda40496fd765dd, not stripped

	It says it's dynamically linked and there is a Linux tool that lets us see any library calls during runtime: ltrace.
	So if we use it:
		$ ltrace ./check
		__libc_start_main(0x804853b, 1, 0xffffd784, 0x8048610 <unfinished ...>
		printf("password: ")                                                                                                             = 10
		getchar(1, 0, 0x65766f6c, 0x646f6700password: test
		)                                                                                            = 116
		getchar(1, 0, 0x65766f6c, 0x646f6700)                                                                                            = 101
		getchar(1, 0, 0x65766f6c, 0x646f6700)                                                                                            = 115
		strcmp("tes", "sex")                                                                                                             = 1
		puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
		)                                                                                             = 29
		+++ exited (status 0) +++

	Now we see some stuff that the executable does, first prints "password: ", then reads the first 3 characters using getchar() and then compares this characters with "sex" using strcmp(chars, "sex").

	So to solve this we just have to input a string starting with "sex", ie: sexasdfsadfasdfsda will be counted as correct.

	From where is the same as before, read the /etc/leviathan_pass file.
}


Leviathan 2 {
	leviathan2:ougahZi8Ta

	We have an executable named printfile in the home directory, that prints a file duh, BUT with some caveats:
		it has to be readable by the user.

	we can see this runing the executable with the ltrace command:
		$ ltrace ./printfile /etc/leviathan_pass/leviathan3
		__libc_start_main(0x804852b, 2, 0xffffd734, 0x8048610 <unfinished ...>
		access("/etc/leviathan_pass/leviathan3", 4)                                                                                      = -1
		puts("You cant have that file..."You cant have that file...
		)                                                                                               = 27
		+++ exited (status 1) +++

	On the second line it uses the acces function with the entered file and 4 (R_OK, read ok) as arguments and returns -1 if its not readable and 0 if it is.
	So if the file is readable it will continue with the program and print it.

	Lets try with a file we own (prev. created the file and directory):
		$ ltrace ./printfile /tmp/pleb/test_file
		__libc_start_main(0x804852b, 2, 0xffffd764, 0x8048610 <unfinished ...>
		access("/tmp/pleb/test_file", 4)                                                                                                 = 0
		snprintf("/bin/cat /tmp/pleb/test_file", 511, "/bin/cat %s", "/tmp/pleb/test_file")                                              = 28
		geteuid()                                                                                                                        = 12002
		geteuid()                                                                                                                        = 12002
		setreuid(12002, 12002)                                                                                                           = 0
		system("/bin/cat /tmp/pleb/test_file"This is a test
		 <no return ...>
		--- SIGCHLD (Child exited) ---
		<... system resumed> )                                                                                                           = 0
		+++ exited (status 0) +++

	As we can see there is no problem and prints the file:
		system("/bin/cat /tmp/pleb/test_file"This is a test

	Now lets try with a file name with some spaces in it and see what happens:
		$ ltrace ./printfile /tmp/pleb/file1\ file2
		__libc_start_main(0x804852b, 2, 0xffffd754, 0x8048610 <unfinished ...>
		access("/tmp/pleb/file1 file2", 4)                                                                                               = 0
		snprintf("/bin/cat /tmp/pleb/file1 file2", 511, "/bin/cat %s", "/tmp/pleb/file1 file2")                                          = 30
		geteuid()                                                                                                                        = 12002
		geteuid()                                                                                                                        = 12002
		setreuid(12002, 12002)                                                                                                           = 0
		system("/bin/cat /tmp/pleb/file1 file2"/bin/cat: /tmp/pleb/file1: No such file or directory
		/bin/cat: file2: No such file or directory
		 <no return ...>
		--- SIGCHLD (Child exited) ---
		<... system resumed> )                                                                                                           = 256
		+++ exited (status 0) +++

	This is more interesting, as we can see in the 7th line first tries to print this file /tmp/pleb/file1 and then the file /file2.
	We can use this as an exploit to print the password for the next level, how?¿ with a symbolic link.
	First we create a symlink to the password:
		$ ln -s /etc/leviathan_pass/leviathan3 file1

	We name the link as file1 because like this it will print it whe we use this command: ./printfile /tmp/pleb/file1\ file2

	And we finally try to print the password:
		$ ./printfile /tmp/pleb/file1\ file2
		Ahdiemoo1j
		/bin/cat: file2: No such file or directory

	Finally we have the password!
}

Leviathan3 {
	leviathan3:Ahdiemoo1j

	In this level we have an executable called level3.

	Let's try to execute it and see what happens:
		$ ./level3
		Enter the password> test
		bzzzzzzzzap. WRONG

	So it ask for a password, now lets try running the executable again but using ltrace also:
		$ ltrace ./level3
		__libc_start_main(0x8048618, 1, 0xffffd784, 0x80486d0 <unfinished ...>
		strcmp("h0no33", "kakaka")                                                                                                       = -1
		printf("Enter the password> ")                                                                                                   = 20
		fgets(Enter the password> test
		"test\n", 256, 0xf7fc55a0)                                                                                                 = 0xffffd590
		strcmp("test\n", "snlprintf\n")                                                                                                  = 1
		puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
		)                                                                                                       = 19
		+++ exited (status 0) +++

	We enter the password and then it compares it to "snlprintf" using strcmp. So if we enter "snlprintf" as the password:
		Enter the password> snlprintf
		[You've got shell]!
		$ whoami
		leviathan4
		$ cat /etc/leviathan_pass/leviathan4
		vuH0coox6m

	And level finished!
}

Leviathan4 {
	leviathan4:vuH0coox6m

	On this level we have a hidden directory named .trash, inside there is an executable called bin.
	If we execute it we get the following:
		$ ./bin
		01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 

	This executable prints an 11 character string in binary.
	If we use ltrace to see if there is comething else going on:
		$ ltrace ./bin
		__libc_start_main(0x80484bb, 1, 0xffffd774, 0x80485b0 <unfinished ...>
		fopen("/etc/leviathan_pass/leviathan5", "r")                                                                                     = 0
		+++ exited (status 255) +++

	So it opens the /etc/leviathan_pass/leviathan5 file and it's probably what is printing in binary, now we just have to convert it into ascii.

	These commands do just this:
		$ echo AB | perl -lpe '$_=join " ", unpack"(B8)*"'
		01000001 01000010
		$ echo 01000001 01000010 | perl -lape '$_=pack"(B8)*",@F'
		AB

	Commands from: https://unix.stackexchange.com/questions/98948/ascii-to-binary-and-binary-to-ascii-conversion-tools

	And using them for our case:
		$ echo 01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 | perl -lape '$_=pack"(B8)*",@F'
		Tith4cokei

	Finally wehave the password for the next level!
}

Leviathan5 {
	leviathan5:Tith4cokei

	There's an executable named leviathan5 on the home directory that opens a file (/tmp/file.log) and prints it, once done it deletes it.

	The get the password for the next level we just have to make the a symlink for "/etc/leviathan_pass/leviathan5" named "/tmp/file.log".

	Then we just have to run the executable.
}

Leviathan6 {
	leviathan6:UgaoFee4li

	There is an executable named leviathan6 on the home directory that	asks for a 4 digit code (0000..9999)

	To pass this level I used a python script to brute-forece the combination, the script is named "leviathan6.py"

	The code was 7123.

	This post helped a lot when creating the script: https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python
}

Leviathan7 {
	leviathan7:ahy7MaeBo9

	There is only a file named "CONGRATULATIONS"
}

Leviathan Finished!