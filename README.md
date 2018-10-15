# nightowlcli

Night Owl CLI - a stub folder structure for Python 3 CLIs

## what?

This is a bare-bones CLI skeleton inspired by (totally ripped off from) a post titled "[The easy (and nice) way to do CLI apps in Python][easy-way-to-do-cli]" by Thomas Stringer with some testing bits snaked from [Python Unit Testing – Structuring Your Project][unit-testing].

### in the box

- Python 3
- Best-practice folder structure (for now)
- Tests (using unittest)
- install scripts

### folder structure and files

```
nightowlcli/
├── README.md           # what it is, include lots of examples, fewer words
├── install.bat         # lazy script to pip3 install (because Windows)
├── install.sh          # lazy script to pip3 install (because Linux/Mac)
├── nightowlcli         # the guts
  ├── __init__.py       # empty, tells Python the folder is a module
  ├── __main__.py       # entry point, do arg parsing here
  └── funky.py          # the code
├── test                # folder for your tests
  ├── __init__.py       # empty, tells Python the folder is a module (yes, even for tests)
  └── test_funky.py     # tests for funky
└── setup.py            # needed to install the cli
```

## why?

I write a lot of these and invariably forget some detail or best practice that I swore I'd totally always remember that I then promptly forgot. My favorite form of procrastination is two hour squirrel adventures searching for the "right way" to do things so for my future self... "ha, get back to work arsehole, we've already been down this rabbit hole."

The more I code the more I become a fan of opinioned languages, frameworks and software free of all the wishy washy "you can put it here, or here, or here" which is all fine and dandy for the long time disciples but when just starting out nothings more frustrating than multiple options with no direction.

## how?

Clone and rename the root folder (nightowlcli) and the code module subfolder (also nightowlcli) as you desire. Toss funky.py and test_funky.py, those are examples and your code is better.

Nothing about this structure is sacred but it is fairly common and it hasn't failed me yet.

### don't forget to...

- update `setup.py` with your information, not mine, unless you're me
- replace the LICENCE file and test in setup.py to match whatever license you're using. I use MIT because it's simple
- Delete everything in this `README.md`, insert your magic. I strongly suggest you at least include:
  - How to install it, assuming the barest knowledge of Python
  - Lots of examples and for all flags/options, at least 2-3 examples ranging from basic to kung fu master. No one reads docs, you hate writing it and no one really likes to wade through tests to see example usage.

[easy-way-to-do-cli]: https://medium.com/@trstringer/the-easy-and-nice-way-to-do-cli-apps-in-python-5d9964dc950d
[unit-testing]:https://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/