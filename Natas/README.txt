Host: http://natasX.natas.labs.overthewire.org/

Natas0 {
	natas0:natas0

	The page says the password for the next level is on it, to see just view the source code.
}

Natas1 {
	natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto

	For this level right clicking has been blocked but to view the source code we can just type: "view-source:" in front of the url.
}

Natas2 {
	natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

	For this level the page says ther is nothing on it but we can look at the source code to make sure:
		<body>
		<h1>natas2</h1>
		<div id="content">
		There is nothing on this page
		<img src="files/pixel.png">
		</div>
		</body></html>

	There is an image named "pixel.png" and it's on the files folder, let's check and see whats inside:
	Inside the folder there is a file named "users.txt" that contains some usernames and passwords, includeing natas3.
}

Natas3 {
	natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

	For this level the source code says:
		<!-- No more information leaks!! Not even Google will find it this time... -->

	First i tried to run gobuster with a small directory list to see if i would find something, SPOILER, i did not.
	Next thing i tried is to google the solution, yeah, yeah, i said i wouldn't do it anymore but idk i was bord.

	To the point once i found the solution i tried to find a way to get there so i googled for common file names on websites, and i found these:
		favicon.ico
		index.html
		robots.txt

	So i tried these files, the first one didn't exist, at least on the main directory; the second one was the main page; and the last one had some juicy stuff:
		User-agent: *
		Disallow: /s3cr3t/

	The file disallowed some folder an i went to it, inside there was a "users.txt" file with the password for the next level.
}

Natas4 {
	natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

	For getting the password for the next level the page says that i have to come from http://natas5.natas.labs.overthewire.org/, weird.
	It just says that i have to come from that site not that i have to be authorized on the site, so i have to create a link on natas5 that redirects me to natas4.

	How to do it, i just copied the line of code for the refresh line and changed index.php fo the whole website:
		On natas4:
			<a href="index.php">Refresh page</a>
		On natas5:
			<a href="http://natas4.natas.labs.overthewire.org/index.php">Refresh page</a>

	I wrote this line of code on the same place as natas4, indide <div id="viewsource">···</div>

	Finally i just had to click the refresh page button on natas5.
}

Natas5 {
	natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

	This level said that i wasn't logged in, so i decided to open the developer tools (F12) and see if i could find anything.

	After a while i found that on the network tab the file "index.php" had a cookie named loggedin set to 0, so i just had to change it to 1.

	To do so i used a Firefox extension named Cookie Quick Manager, just go to natas5 and click the extension then search for cookies on the current site an modify value.
	Finally refresh the page and done.
}

Natas6 {
	natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

	For this level i'll have to sumbit a string and the web will check if it's correct if it is it will give me the next password.
	Luckily we can view the source code:
		<?

		include "includes/secret.inc";

		    if(array_key_exists("submit", $_POST)) {
		        if($secret == $_POST['secret']) {
		        print "Access granted. The password for natas7 is <censored>";
		    } else {
		        print "Wrong secret";
		    }
		    }
		?>

	This code first includes the file "includes/secret.inc", then checks if the user has sent any data and finally if the value we entered is equal to $secret the next password is given.

	If we go to the file "includes/secret.inc" we find this:
		<?$secret = "FOEIUWGHFEEUHOFUOIU";?>

	It's the variable $secret we need!

	And if we enter this and sumbit it we get the next password.
}

Natas7 {
	natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
}
