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
}


Leviathan 2 {
	leviathan2:ougahZi8Ta
}