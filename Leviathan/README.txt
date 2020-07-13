Host: leviathan.labs.overthewire.org:2223

Leviathan0 {
	leviathan0:leviathan0

	there is a hidden directory on the main folder named .backups, inside there is a file named bookmarks.html:
		bookmarks.html: HTML document, ASCII text, with very long lines

	if we search for leviathan inside the file we found this at line 1049:
		<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
}

Leviathan1 {
	leviathan1:rioGegei8m

	There is a program called check that asks you for a password.
	I read a hint that said that this level would be easy for people who watched Hackers(film) so i decided to look at the hacks from the movie,
	first link and first hack i read was about the most common passwords such as:
		password, 123456, love, secret, god, sex
	
	I tried this passwords and it was the las one.
	Now the program executes a shell in which you are leviathan2, so just read the password form /etc/leviathan_pass/
}

Leviathan 2 {
	leviathan2:ougahZi8Ta
}