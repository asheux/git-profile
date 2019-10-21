# git-profile

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
$ python3 -m pytest
```

- Run application

```
$ python run.py
```

### Test application

- On postman

- [http://127.0.0.1:5000/repos/pygame](http://127.0.0.1:5000/repos/pygame)
- [http://127.0.0.1:5000/repos/mailchimp](http://127.0.0.1:5000/repos/mailchimp)

- Using curl command

```
$ curl -i http://127.0.0.1:5000/repos/pygame
```

- Expected response

```
{
    "result": {
        "languages": 4,
            "public_repos": {
                "forked_repos": 1,
                "original_repos": 12
            },
            "topics": 11,
            "watchers": 1802
    }
}
```
