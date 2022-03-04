# Regular Expressions

## Table of Contents <!-- omit in toc -->

1. [Activities](#activities)
1. [Objectives](#objectives)
1. [Resources](#resources)
1. [Practice Challenges](#practice-challenges)
1. [Challenges](#challenges)
1. [Stretch Challenges](#stretch-challenges)

## Activities

- Code review implementations of higher order Markov chains
- Review structures used to build Markov chain and discuss scalability
- Lecture and discussion following [regular expressions slides]
- Build and test regular expressions with [RegExr] and visualize them with [RegExper]

## Objectives

After completing this class session and the associated tutorial challenges, students will be able to ...

- Use regular expressions to clean up and remove junk text from corpus
- Use regular expressions to create a more intelligent word tokenizer

## Resources

- Watch Make School's [regular expressions lecture]
- Review Make School's [regular expressions slides]
- Use Cheatography's [regular expressions cheat sheet] as a reference guide
- Solve interactive challenges in UBC's [regular expressions lab webpage][ubc regex lab]
- Use [RegExr] or [RegEx Pal] to build and test regular expression patterns on text samples
- Use [RegExper] to visualize railroad diagrams of regular expression patterns
- Read StackOverflow answers to questions about using regular expressions to parse HTML: first [some comedic relief][so match html tags] and then [an explanation of why you shouldn't][so why not html]

## Practice Challenges

**INSTRUCTIONS**: Open RegExr ([https://regexr.com/][regexr]) and paste this document into the box labeled "Text", then try to come up with a regular expression pattern to match all of the examples to the right of each challenge description.

1. Match a lowercase letter (a, r, g, h, not A, R, G, H)
2. Match a lowercase word (little, words, not Names, CONSTANTS)
3. Match an UPPERCASE word (ARGGHHH, I, PIZZA, ZZZZ, not ARGgHHH, Pizza)
4. Match a Capitalized word (A Bear of Very Little Brain)
5. Match 3 Capitalized words (Very Little Brain, not Pooh Bear)
6. Match 1 or more words (any case, Mixed cAsE woRDs CounT toO)
7. Match an integer (5, 42, 888, 0, -345, +55, +-42, -+42)
8. Match a decimal number (3.14, 123.456, -8.42, 10., 0.)
9. Match a money amount ($5, $8.42, $12,345,678.90, $42,15, $4,1500,00)
10. Match a valid variable name (snake_case_12, camelCase2004, ClassName, crazy_Case)
11. Match a valid US phone number (555-1234, 415-555-1234, (415) 555-1212)
12. Match a valid email address (foobar@gmail.com, reg.ex+wiz.ard@jmail.co.jp)
13. Match a valid ISO-formatted date (2017-10-20)
14. Match a valid US-formatted date (12/25, 10/20/2017, Oct 20 2017)

## Challenges

These challenges are the baseline required to complete the project and course. Be sure to complete these before next class session and before starting on the stretch challenges below.

- [Page 13: Parsing Text and Clean Up]

  - Remove unwanted junk text (e.g., chapter titles in books, character names in scripts)
  - Remove unwanted punctuation (e.g., `_` or `*` characters around words)
  - Convert HTML character codes to ASCII equivalents (e.g., `—` to `—`)
  - Normalize punctuation characters (e.g., convert both types of quotes – `‘’` and `“”` – to regular quotes – `''` and `""`)

- [Page 14: Tokenization][page 13: parsing text and clean up]

  - Handle special characters (e.g., underscores, dashes, brackets, `$`, `%`, `•`, etc.)
  - Handle punctuation and hyphens (e.g., `Dr.`, `U.S.`, `can't`, `on-demand`, etc.)
  - Handle letter casing and capitalization (e.g., `turkey` and `Turkey`)

## Stretch Challenges

These challenges are more difficult and help you push your skills and understanding to the next level.

- [Page 13: Parsing Text and Clean Up]

  - Make your parser code readable, then improve its organization and modularity so that it's easy to modify in the future
  - Modify your parser so that it can be used as both a module (imported by another script) and as a stand-alone, executable script that, when invoked from the command line with a file argument, will print out the cleaned-up version, which can be redirected into a file

- [Page 14: Tokenization][page 13: parsing text and clean up]

  - Make your tokenizer code readable, then improve its organization and modularity so that it's easy to modify in the future
  - Write tests to ensure that you're getting the results you've designed for, then run your tests with controlled input data
  - Come up with at least one other tokenization strategy and compare performance against your original strategy, then find ways to make your tokenizer more efficient

[page 13: parsing text and clean up]: https://bit.ly/tutorial-tweet-generator
[page 14: tokenization]: https://bit.ly/tutorial-tweet-generator
[regex pal]: https://www.regexpal.com/
[regexper]: https://regexper.com/
[regexr]: https://regexr.com/
[regular expressions cheat sheet]: https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/
[regular expressions lecture]: https://www.youtube.com/watch?v=roUtBDH3Obc
[regular expressions slides]: https://github.com/tech-at-du/ACS-1120-Intro-Data-Structures/blob/master/Slides/RegularExpressions.pdf
[so match html tags]: http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags
[so why not html]: http://stackoverflow.com/questions/590747/using-regular-expressions-to-parse-html-why-not
[ubc regex lab]: http://www.ugrad.cs.ubc.ca/~cs121/2015W1/Labs/Lab8/lab8.html
