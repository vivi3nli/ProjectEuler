# [ProjectEuler](https://projecteuler.net/)
All the problems from project euler. Recommand solving it yourselves before searching for a solution. After solving every solution there's a Project Euler problem overview for every problem.
##[Problem 1](https://projecteuler.net/problem=1)
`Find the sum of all the multiples of 3 or 5 below 1000`
The way I did was straight forward with a loop and might be slow when the upper bond is incremented. 
The fastest way is doing it mathmatically to calculate the answer directly. Also using python `set`
can get the result within on line which is quite short.
##[Problem 2](https://projecteuler.net/problem=2)
`By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.`
First I wanted to append it to a list in order to save the numbers, but it seemed not working out. The second try was to ust recursion. While by analysing the occurance it's most efficient by add up every 3 numbers.