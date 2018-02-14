# A tiny flask web app blueprint

This a basic `python3` [flask webapp](http://flask.pocoo.org/) blueprint for quickly adding a web interface to your python scripts. What you get:

- A [flask webapp](http://flask.pocoo.org/) organized as a python package following the [larger applications template](http://flask.pocoo.org/docs/0.12/patterns/packages/#larger-applications).
- A html template starting point using [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/) to extend for pretty, modern and responsive webpages!
- A [Dockerfile](Dockerfile) to build your very own container and easily deploy it anywhere.

## Start here

First, clone this repository `git clone https://github.com/cmsirbu/tiny-flask` or [download a zip file](https://github.com/cmsirbu/tiny-flask/archive/master.zip). You don't really need the whole git part as this is the start of an application of your own!

Then, to develop locally, the cleanest way to do it is with a [python virtualenv](https://docs.python.org/3/tutorial/venv.html). Make sure you have `python3` and `pip3` installed, then run the commands below (only once, for setup):

```
# make sure you're in the repository you just downloaded
cd tiny-flask
# create a virtualenv and activate it
pyvenv venv
source venv/bin/activate
# update the tools
pip install -U pip setuptools
# install the tiny-flask package in the venv with its dependencies
pip install -e .
```

Once you have that set up, you can start the application in development mode anytime using:

```
# activate the virtualenv (only if it's not already)
source venv/bin/activate
# start flask's development webserver
FLASK_APP=tinyflask flask run
```

You should see a message like this:

```
 * Serving Flask app "tinyflask"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now open `http://127.0.0.1:5000/` in your browser:

![Screenshot](ss.png)

Success!

## Running the webapp in production

The built-in server offered by `flask` is only useful for development and serves only one request at a time by default - read about flask [deployment options](http://flask.pocoo.org/docs/0.12/deploying/#deployment).

Therefore, in order to actually serve multiple clients concurrently, one of the solutions in the above deployment link must be used. Ultimately it's up to you, but I've included an example running `gunicorn` to serve requests with the `gevent` async worker (which is more suited to long-running scripts or outgoing requests to other APIs etc.).

### Install in the virtualenv

```
# activate the virtualenv (only if it's not already)
source venv/bin/activate
# install gunicorn and gevent
pip install gunicorn gevent
# run tinyflask
gunicorn tinyflask:app -b 127.0.0.1:5000 --workers 3 -k gevent
[2018-02-14 21:44:21 +0000] [15227] [INFO] Starting gunicorn 19.7.1
[2018-02-14 21:44:21 +0000] [15227] [INFO] Listening at: http://127.0.0.1:5000 (15227)
[2018-02-14 21:44:21 +0000] [15227] [INFO] Using worker: gevent
[2018-02-14 21:44:21 +0000] [15230] [INFO] Booting worker with pid: 15230
[2018-02-14 21:44:21 +0000] [15231] [INFO] Booting worker with pid: 15231
[2018-02-14 21:44:21 +0000] [15232] [INFO] Booting worker with pid: 15232
```

### Build and run a Docker container

Building a container is a bit more involved, but it provides are very nice minimally packaged version of the webapp that can run on any Docker enabled host.

```
# build the container
docker build -t tinyflask:0.1 -f tiny-flask/Dockerfile .
# run it locally
docker run -p 5000:80 -d tinyflask:0.1
# open 127.0.0.1:5000 success!
```

You can save the container image and distribute it locally, publish it to Docker Hub or upload it to a private Docker registry. The sky's the limit!

