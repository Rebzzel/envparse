<h1 align="center">envparse</h1>
<p align="center">
	Argparse, but for environment variables.
	<br/><br/>
	<a href="#">
		<img src="https://img.shields.io/badge/python-3.6%2B-blue.svg"/>
	</a>
</p>
<br/>

- [Usage](#usage)
- [Information](#information)
- [License](#license)

<br/>

## Usage
```py
import os

print(os.environ)
#{
#    ...
#    "SUPER_INT": "1234",
#    "MY_APP$SUPER_INT": "5678",
#    "MY_APP$SUPER_BOOL": "yes",
#    ...
#}

from envparse import EnvironmentParser

def to_bool(value):
    return value.lower() in ("1", "true", "yes", "on")

parser = EnvironmentParser(
    prefix="MY_APP", # default: ""
    prefix_delimiter="$", # default: "_"
)
parser.add("SUPER_INT", transformer=int)
parser.add("SUPER_BOOL", transformer=to_bool)
parser.add("DOES_NOT_EXIST")

env = parser.parse_env()

print(env)
# Namespace(super_int=5678, super_bool=True, does_not_exist=None)

print(env.super_int)
# 5678
```

## Information

### Requirements
- Python `>= 3.6`

### Installation
Using pip:

```
pip install python-envparse
```

or locally:

```
git clone https://github.com/Rebzzel/python-envparse.git
cd python-envparse
pip install .
```


## License
```
MIT License

Copyright (c) 2014-2023 Rebzzel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
