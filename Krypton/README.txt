Host: 

Krypton0 {
	The passowrd for krypton1 is encoded in base64:
		S1JZUFRPTklTR1JFQVQ=

	To decoded we can use the following command:
		$ base64 --decode krypton1_enc > krypton1

	And the password is:
	KRYPTONISGREAT
}

Krypton1 {
	krypton1:KRYPTONISGREAT

	For solving this level we have to go to: /krypton/krypton1
	In this folder there is a README file and the encoded password. The password is encoded using ROT13.

	To decode the password we can use the following command:
		$ tr [A-Z] [N-ZA-M] < krypton2
		LEVEL TWO PASSWORD ROTTEN
}

Krypton2 {
	krypton2:ROTTEN

	Password for the next level is encrypted using a caesar cipher with an unknown key, kinda. The kwy is stored in a keyfile.dat file on the level directory.
	So if we encrypt the alphabet using this key and the encrypt binary we can deduce the used key.
	Doing it we found that the key is 12.

	So we just need to decrypt the krypton3 file using 12 as the key and:
		CAESARISEASY
}

Krypton3 {
	krypton3:CAESARISEASY
}
