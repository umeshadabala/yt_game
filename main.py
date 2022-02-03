import time
print("Welcome to this game")
time.sleep(1)
print("Hey i am Raju your assistant in this game ")
time.sleep(1)
print("i am thinking to start a new tech youtube channel ")
yn= str(input("y/n : "))
if yn == "y":
	print("hmm lets continue the game")
	time.sleep(1)
	print("help me setup my channel")
	time.sleep(1)
	print("pls suggest me name for my channel")
	cn  = str(input("enter channel name : "))
	print(f"our channel name is {cn}")
	time.sleep(1)
	print("now i got an idea of recording a video  ")
	time.sleep(1)
	rec  = str(input("enter rec to start recording : "))
	if rec == "rec":
		print("hmm, we recored my first video ")
		time.sleep(1)
		print("help me edit the video")
		time.sleep(1)
		edit = str(input("type edit to edit the video : "))
		if edit == "edit":
			print("we edited our first video")
			time.sleep(1)
			print("let's upload our video")
			time.sleep(1)
			up = str(input("type upload to upload our first video : "))
			if up == "upload":
				print("we uploaded our first video")
				time.sleep(5)
				print("bye meet you in another game")
				time.sleep(3)
				print("thanks for playing")

			else:
				exit()
		else:
			exit()
	else:
		exit()
	 
elif yn == "n":
	quit()
else:
	exit
