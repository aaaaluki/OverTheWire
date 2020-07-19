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
		$ ltrace /etc/leviathan_pass/leviathan3
		__libc_start_main(0x804852b, 2, 0xffffd734, 0x8048610 <unfinished ...>
		access("/etc/leviathan_pass/leviathan3", 4)                                                                                      = -1
		puts("You cant have that file..."You cant have that file...
		)                                                                                               = 27
		+++ exited (status 1) +++

	On the second line it uses the acces function with the entered file and 4 (R_OK, read ok) as arguments and returns -1 if its not readable and 0 if it is.

	

}
