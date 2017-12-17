# Affine Cipher

## History and usage

The *affine cipher* is a type of monoalphabetic **substitution cipher**. It ecnrypts a text using an *affine function* (ax + b).

## Detailed Explanations : How it works?

1. Firstly, each character of the initial text (message to encrypt) is converted in a number from 0 to 25, corresponding to its position in the Latin alphabet which contains 26 letters --> (a = 0, b = 1 ... z = 25 )
2. Then, each number is transformed by an affine function (ax + b) where x is the number and a and b are the keys required to decrypt the final message. The values of modulo 26 of each image are stored in a new list. (**Modulo means remainder**)
3. Therefore, we convert each number of the list in a letter from the Latin Alphabet according to its position.
4. We finally create the final message by putting all the letters side by side.

Steps 1 and 3 can be done with these tables : 

| A | B | C | D | E | F | G | H | I | J | K  | L  | M  |
|---|---|---|---|---|---|---|---|---|---|----|----|----|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| N  | O  | P  | Q  | R  | S  | T  | U  | V  | W  | X  | Y  | Z  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

## Weaknesses

- As each letter is encrypted using the same function, trying many possibilities for a or b can be useful to decrypt the message This is called the **bruteforce method**.

- We can also use **frequency analysis** if the message is long to decrypt the message as the most common letters in english are :

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/English_letter_frequency_%28alphabetic%29.svg/340px-English_letter_frequency_%28alphabetic%29.svg.png">
</p>

- Other possibilities include guessing the keys a and b

- Knowing a can be helpful to eliminate a lot of solutions

## Example

- Message to encrypt : **ATTACK**
- Function used : f(x) = **3x + 6**
- That means that **a = 3 and b = 6**

Using the above tables, ATTACK can be written as : **0 19 19 0 2 10**
Images of each number :

- f(0) = 6
- f(19) = 63 
- f(2) = 12
- f(10) = 36

The new list is : **6 63 63 6 12 36**

Using the **modulo 26 method**, we obtain:

- Mod(6,26) = 6
- Mod(63,26) = 11
- Mod(12,26) = 12
- Mod(36,26) = 10

The final message is **6 11 11 6 12 10** and using the tables again, we convert them in the encrypted message :

> **GLLGMK**

**ATTACK** is encrypted with the function **3x + 6** and becomes **GLLGMK**.
