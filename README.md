<h1 align="center">CSS IA-1: Audio Steganography</h1>
Steganography is the art and science of secret hiding. The secret message or plain text may be hidden in one various ways. The methods of cryptography render the message unintelligible to the outsider by various transformations of the text whereas the methods of steganography conceal the existence of the message. To conceal a secret message we need a wrapper or container as a host file. Different wrappers or host files or cover medium are used to hide the secret message e.g. image, audio, video, text.
<h1>Project By</h1>

| <h3>Dhairya Shah</h3> | <h3>Peeya Thacker</h3> | <h3>Sameer Wadhwa</h3> |
| -------------------- | ---------------------- | ---------------------- |
| <h3>1911119 </h3>    | <h3>1911127</h3>       | <h3>1911131</h3>       |
| <h3>B4</h3>          | <h3>B4</h3>            | <h3>B4</h3>            |


# Prerequisites

  -   A system running Windows 10/Linux/MacOS
  -   Python IDE
  -   A sample wav file

# Running the project

-   Clone the repository.
    </br>
    -   `git clone https://github.com/dhairya903/CSS-IA-1`
-   Open the project using any python IDE.
-   Make sure to have the sample.wav file in the same directory. (In case of a different .wav file make sure to make the corresponding changes in the python files)



# Algorithms 
-   <b>Standard LSB:</b>
    In this algorithm, we insert the secret information in the LSB position i.e modifying the last one bit of the original bytearray. 
    
-   <b>Modified LSB without flip:</b>
    In this algorithm, we insert the secret information in the 3rd and 4th bit from the LSB i.e modifying 2 bits of the original bytearray. 
    
-   <b>Modified LSB with flip:</b>
    In this algorithm, we insert the secret information in the 3rd and 4th bit from the LSB i.e modifying 2 bits of the original bytearray. Beyond that, the 2 bits of the modified bytearray are then flipped. 





