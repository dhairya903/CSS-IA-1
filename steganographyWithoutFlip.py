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
    print("\nEncoding Starts..")
    audio = wave.open("sample.wav", mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    print('Length of frame(in bytes): ', len(frame_bytes))
    print('First 15 original frame bytes: ')
    for i in range(0, 15):
        print(frame_bytes[i], end=" ")
    string = str(input("\nEnter secret text: "))
    print(string)
    string = string + int(((2*len(frame_bytes))-(len(string)*8*8))/8) * '#'
    bits = list(
        map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    j = 0
    for i in range(0, len(frame_bytes), 2):
        frame_bytes[j] = frame_bytes[j] & 243
        if bits[i] == 0 and bits[i+1] == 1:
            frame_bytes[j] = frame_bytes[j] + 4
        elif bits[i] == 1 and bits[i+1] == 0:
            frame_bytes[j] = frame_bytes[j] + 8
        elif bits[i] == 1 and bits[i+1] == 1:
            frame_bytes[j] = frame_bytes[j] + 12
        j = j + 1
    frame_modified = bytes(frame_bytes)
    print('First 15 modified frame bytes: ')
    for i in range(0, 15):
        print(frame_bytes[i], end=" ")
    newAudio = wave.open('outputWithoutFlip.wav', 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)

    newAudio.close()
    audio.close()
    print("Message succesfully encoded inside outputWithoutFlip.wav")


def decode():
    print("\nDecoding Starts..")
    try:
        audio = wave.open("outputWithoutFlip.wav", mode='rb')
    except FileNotFoundError:
        print('outputWithoutFlip.wav file not found')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    #print('First 15 frame bytes: ')
    # for i in range(0,15):
    #	print(frame_bytes[i], end=" ")

    extracted = []

    for i in range(len(frame_bytes)):
        frame_bytes[i] = frame_bytes[i] & 12
        if frame_bytes[i] == 0:
            extracted.append(0)
            extracted.append(0)
        elif frame_bytes[i] == 4:
            extracted.append(0)
            extracted.append(1)
        elif frame_bytes[i] == 8:
            extracted.append(1)
            extracted.append(0)
        elif frame_bytes[i] == 12:
            extracted.append(1)
            extracted.append(1)
    string = "".join(chr(
        int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    print("Sucessfully decoded: "+decoded)
    audio.close()


while(1):
    print("\nSelect an option: \n1)Encode\n2)Decode\n3)Exit")
    val = int(input("\nChoice:"))
    case(val)
