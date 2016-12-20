# Purchase Order Generator - POGen

## How to deploy?

First, build an image
```
make docker-build
```

Then, run it
```
make docker-run
```

It will create a sqlite3 file in your working directory.
If you run this for first time, you need to initialize database
```
make docker-init-database
```
