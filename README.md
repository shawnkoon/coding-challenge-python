# coding-challenge-python

| Master                                                                                                                                                | Versioning                                                                                                                                  | Quality                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![Build Status](https://travis-ci.com/shawnkoon/coding-challenge-python.svg?branch=master)](https://travis-ci.com/shawnkoon/coding-challenge-python) | [![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=shawnkoon/coding-challenge-python)](https://dependabot.com) | [![CodeFactor](https://www.codefactor.io/repository/github/shawnkoon/coding-challenge-python/badge)](https://www.codefactor.io/repository/github/shawnkoon/coding-challenge-python) |

Coding challenge practice using python 3.

## Key Points

-   ### 🎯 Algorithms & DataStructure
-   ### 🎯 Continuous Integration
-   ### 🎯 Problem Solving
-   ### 🎯 Test Driven Development (TDD)
-   ### 🎯 Python
-   ### 🎯 Fun?

## How to run

1. I highly recommend using `virtualenv` before continuing.

1. Install necessary **dependencies**.

```bash
$ make install

...
```

2. Run **all** the tests.

```bash
$ make ci

...
```

3. Run **specific** test.

```bash
$  make test module=<module_name>   // ex) make test module=hello_world

...
```

## VS Code settings

If using `virtualenv`, add following settings to vscode file. _(Replace content within <>)_

```javascript
{
  "python.pythonPath": "<Value you get from running 'which python'>"
}
```
