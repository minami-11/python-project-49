### Description:
Here is the Brain Games pack. The pack contains 5 games:
1. brain-even: guess is number even or odd
2. brain-calc: guess the result of math expression
3. brain-gcd: guess the greatest common divisor of given number
4. brain-progression: guess the number is missing in arithmetic progression
5. brain-prime: guess whethere number is prime or not

#### Game process is pretty simple:
* 3 Correct answers and You win. 1 wrong answer and You lose 

#### Installation process and commands:
Staying in the root project directory use these commands:
```
make build 		#poetry build distribution package file in .whl format
make package-install	#pip install Brain-Games pack from .whl file
```
No errors occured - the installation has been success.

```
make package-uninstall  #pip uninstall the Brain-Games pack
```

#### Other commands for devepolers:
```
make lint		#check quality of Python Code with flake8
make shell		#enter virtual env
make publish		#perform all actions for publishing, except uploading the package
make automate_build	#start commans 1by1: shell, lint, build, publish, pip list
make brain-games	#poetry will start brain-games
make brain-<game_name>	#poetry will run one of these games: even, calc, gcd, progression, prime
```
 

#### Hexlet tests, linter status and CodeClimate marks:
[![Actions Status](https://github.com/minami-11/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/minami-11/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1b7630544f96183d8c54/maintainability)](https://codeclimate.com/github/minami-11/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1b7630544f96183d8c54/test_coverage)](https://codeclimate.com/github/minami-11/python-project-49/test_coverage)


### Installation:
[![asciicast](https://asciinema.org/a/y4mBHr5ESINsNhf5B4G17ylmQ.svg)](https://asciinema.org/a/y4mBHr5ESINsNhf5B4G17ylmQ)

### How Brain Games works:
[![asciicast](https://asciinema.org/a/vi1HcnTdoAcE4lHKIwe0Q5rki.svg)](https://asciinema.org/a/vi1HcnTdoAcE4lHKIwe0Q5rki)
