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
}
