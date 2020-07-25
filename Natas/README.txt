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
}