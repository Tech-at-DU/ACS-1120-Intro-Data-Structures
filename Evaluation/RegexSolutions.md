# RegEx Practice Challenge Solutions

**INSTRUCTIONS**: Open RegExr ([<https://regexr.com/][regexr>]) and paste this document into the box labeled "Text", then try to come up with a regular expression pattern to match all of the examples to the right of each challenge description.

1. **Match a lowercase letter**: `[a-z]`
2. **Match a lowercase word**: `\b[a-z]+`
3. **Match an UPPERCASE word**: (`AGGHHH`, `A`, `I`, `ZA`, `ZZZZ`, not `aGGHH`)**: `\b[A-Z]+\b`
4. **Match a Capitalized word**: (`A Bear of Very Little Brain`)_*: `\b[A-Z][a-z]_\b`
5. **Match 1-3 Capitalized words**: (`Very Little Brain`, not `Pooh Bear`)_*: `((\b[A-Z][a-z]_\b)\W){1,3}`
6. **Match 1 or more words (any case, Mixed cAsE woRDs CounT toO)**: `\b[A-Za-z]+(\s[A-Za-z]+)*\b`
7. **Match an integer (`5`, `42`, `888`, `0`, `-345`, `+55`, `+-42`, `-+42`)**: `[-+]?\d+`
8. **Match a decimal number (`3.14`, `123.456`, `-8.42`, `10.`, `0.`)**: `[+-]?\d+(.\d*)?`
9. **Match a money amount (`$5`, `$8.42`, `$12,345,678.90`, `$42,15`, `$4,1500,00`)**: `\$\d{1,3}(,\d{3})*(.?\d{2})?`
10. **Match a valid variable name** (`snake_case_12`, `camelCase2004`, `ClassName`, `crazy_Case`): `TODO`
11. **Match a valid US phone number** (`555-1234`, `415-555-1234`, `(415) 555-1212`): `TODO`
12. **Match a valid email address** (`foobar@gmail.com`, `reg.ex+wiz.ard@jmail.co.jp`): `TODO`
13. **Match a valid ISO-formatted date** (`2017-10-20`): `TODO`
14. **Match a valid US-formatted date** (`12/25`, `10/20/2017`, `Oct 20 2017`): `TODO`
