# Purchase Order Generator - POGen

## How to deploy?

### With docker
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

### Without docker

First, you need to install dependencies
```
yum install python34 python34-pip
pyp3 install -r requirements.txt
```

Then, if you want it to listen in port `8080`
```
make run
```

Alternatively, you can run it listeninig port `80`
```
make run-80
```
