import wave

def case(a):
	if a == 1:
		encode()
	elif a == 2:
		decode()
	elif a == 3:
		quit()
	else:
		print("\nEnter valid Choice!")

def encode():
	try:
		# Opening audio file in read only mode
		audio = wave.open("sample.wav",mode="rb") 
	except FileNotFoundError:
		print('sample.wav file not found')
		return
	# Reads and returns at most n frames of audio, as a bytes object which is stored in bytearray
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	print('Length of frame(in bytes): ',len(frame_bytes))
	print('First 15 original frame bytes: ')
	for i in range(0,15):
		print(frame_bytes[i], end=" ")
	string = input('\nEnter secret text: ')
	print("\nEncoding Starts...")
	string = string + int((len(frame_bytes)-(len(string)*8*8))/8) * '#'
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
	print('Length of bits: ',len(bits))
	for i, bit in enumerate(bits):
	    frame_bytes[i] = (frame_bytes[i] & 254) | bit
	frame_modified = bytes(frame_bytes)
	print('First 15 modified frame bytes: ')
	for i in range(0,15):
		print(frame_bytes[i], end=" ")
	# Opening audio file in write only mode
	newAudio =  wave.open('output.wav', 'wb')
	newAudio.setparams(audio.getparams())
	newAudio.writeframes(frame_modified)

	newAudio.close()
	audio.close()
	print("\nMessage succesfully encoded inside output.wav")

def decode():
	print("\nDecoding Starts..")
	try:
		audio = wave.open("output.wav", mode='rb')
	except FileNotFoundError:
		print('output.wav file not found')
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	print('First 15 frame bytes: ')
	for i in range(0,15):
		print(frame_bytes[i], end=" ")
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	decoded = string.split("###")[0]
	print("\nSucessfully decoded: " + decoded)
	audio.close()

while(1):
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)exit")
	val = int(input("\nChoice:"))
	case(val)
