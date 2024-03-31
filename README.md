## Time Spent:
I spent about 30 minutes looking over the challenge documentation, brainstorming solutions, and setting up my environment. I spent a little less than an hour implementing and testing my solution in Python, and now expect to spend about 15 minutes preparing my submission in GitHub. Due to personal time contraints, my goal was to spend at most an hour and a half on the challenge.
## Process:
Once I understood that subtractive notation can only involve two symbols, a solution for converting roman numerals to decimal became immediately clear. I could step through every combination of two symbols in the roman numeral string and see if the decimal value of the first was less than the decimal value of the second. If so, I could add the difference between the two symbols to my total and remove the symbols from the string. If subtractive notation was not taking place, I could simply add the decimal value of the first symbol to the total and remove it from the string. I repeated this process until the roman numeral string was empty. This simple algoritm only took a few minutes to implement and test.

The problem of converting decimal to roman numerals was more complicated. The rules dictating which symbols could precede other symbols seemed unclear and difficult to implement. Instead of creating a complicated algorithm, I opted for simplicity and identified illegal combinations of roman numerals and their legal counterparts. Any time an illegal combination is detected at the end of the roman numeral string, it is replaced by the legal equivalent. Any time a symbol is added to the growing roman numeral string, its decimal value is subtracted from the decimal number that is being converted. This process is repeated until the decimal number is 0. It isn't the most elegant solution, but it fit my needs.
Finally, I implemented a few lines of code to allow my solution to run from the command line. Running main.py without any arguments will explain the syntax for running conversions.
## Further Work:
If I had more time, I would brainstorm a better (i.e. less verbose) algorithm for decimal to roman numeral conversion. This would be essential to allow my program to work with roman numerals greater than 3999. Additionally, I would add code to verify that roman numerals input by the user were valid. I would also improve the user experience by adding better instructions.
