# RSABasic

**_What is RSA?_**

RSA is an asymptotic encryption algorithm that uses a public-key to encrypt a message and a private key to decrypt a message. RSA is a good encryption algorithm because it uses 2 very large prime numbers as the starting point for the encryption process. Cracking the RSA encryption is very difficult, and needless to say it is very computational and time consuming. This means that only you, with your private key, can decrypt an encrypted message sent to you.


This program is a simple and clean implementation of the RSA encryption algorithim in Python.

Dependencies:
-  Random


The function test() is the driver of the program. 

To run the program call the function test() with your message as an argument:

![image](https://user-images.githubusercontent.com/85080576/149442203-651d14e3-cbe8-43ba-a490-906407c8413e.png)

Output: 

![image](https://user-images.githubusercontent.com/85080576/149442147-fb907108-d248-4101-9a2d-ad8dbea741e6.png)



To view the public and private keys, as well as the encrypted and decrypted messages, pass in verbose=true as an argument to the function test() when calling it.

![image](https://user-images.githubusercontent.com/85080576/149442246-de36375b-51ad-4596-ae21-26f1cd0f2ee2.png)

Output:

![image](https://user-images.githubusercontent.com/85080576/149637639-bec25ade-8dd0-4ad5-9c67-dc8b02ab2f6f.png)
