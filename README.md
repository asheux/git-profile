# git-profile

![Travis](https://travis-ci.com/asheuh/git-profile.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/asheuh/git-profile/badge.svg?branch=master)](https://coveralls.io/github/asheuh/git-profile?branch=master)

### Setup application

- Clone repo

```
$ git clone https://github.com/asheuh/git-profile.git
$ cd git-profile
```

- Virtual Environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

- Install requirements

```
$ pip install -r requirements.txt
```

- Run tests

```
$ py.test --cov=app tests/
```

- Run application

```
$ python3 run.py
```

### Test application

- On postman

- [http://127.0.0.1:5000/api/v1/repos/pygame](http://127.0.0.1:5000/api/v1/repos/pygame)
- [http://127.0.0.1:5000/api/v1/repos/mailchimp](http://127.0.0.1:5000/api/v1/repos/mailchimp)

- Using curl command

```
$ curl -i http://127.0.0.1:5000/api/v1/repos/pygame
```

- Sample response

```
{
    "result": {
        "languages": [
            "c++",
            "python",
            "c",
            "ruby"
        ],
        "public_repos": {
            "forked_repos": 1,
            "original_repos": 12
        },
        "topics": 11,
        "watchers": 1820
    }
}
```
