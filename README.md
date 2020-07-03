# highly-composite-numbers

## Overview

A **H**ighly **C**omposite **N**umber (**HCN**) is a **natural number** which has more **factors** than all the numbers before it. 
For example:

`1` has *one* factor, `1`, and is the first number - therefore it is a **HCN****.

`2` has *two* factors, `1` and `2`, which is more than `1` - therefore is a **HCN**.

etc

## The Code

Originially the code checked every natural number. 
It finds all the factors of each number and records them in a list. This length of this list is then checked against the number of factors from the previous HCN to see which has more.
If the new number has **more** factors than the last HCN then it is a HCN, and its factors are recorded as the latest HCN.

Unfortunately, HCNs get very large very quickly and therefore a program which checks every single natual number is very slow.
Improvements needed to be made.

## Improvements

The following theories about HCNs have been proved and can be used to make the program more efficient.

### It must be divisible by 6 to be a HCN

Except for `1`, `2` and `4` which are the first 3 HCNs, a number must be divisible by 6 in order to be a HCN. 

Using this, we now only need to check every 6th number which makes the program more efficient.

### HCNs greater than 36 cannot be square numbers

We now only need to check up to the square root of a number when looking for factors.

## Records

This program also outputs a `.txt` file which contains each HCN, its factors and its prime factorisation.