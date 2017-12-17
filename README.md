# Affine Cipher

## History and usage

The affine cipher is a type of monoalphabetic substitution cipher. It ecnrypts a text using an affine function (ax + b).

## Deatailed Explanations : How it works?

1. Firstly, each character of the initial text (message to encrypt) is converted in a number from 0 to 25, corresponding to its position in the Latin alphabet which contains 26 letters --> (a = 0, b = 1 ... z = 25 )
2. Then, each number is transformed by an affine function (ax + b) where x is the number and a and b are the keys required to decrypt the final message. The values of modulo 26 of each image are stored in a new list. (Modulo means remainder)
3. Therefore, we convert each number of the list in a letter from the Latin Alphabet according to its position.
4. We finally create the final message by putting all the letters side by side.

## Weaknesses

- As each letter is encrypted using the same function, trying many possibilities for a or b can be useful to decrypt the message This is called the bruteforce method.

- We can also use frequency analysis if the message is long to decrypt the message as the most common letters in english are :

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/English_letter_frequency_%28alphabetic%29.svg/340px-English_letter_frequency_%28alphabetic%29.svg.png">
</p>

- Other possibilities include guessing the keys a and b

- Knowing a can be helpful to eliminate a lot of solutions

## Examples





