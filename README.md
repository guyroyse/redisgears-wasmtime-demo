# Python, RedisGears, and Wasmtime

This is a rough bit of sample code for invoking WebAssembly modules from within Redis using RedisGears and Wasmtime.

## Abbreviated Instructions

### Redis

Make sure you have Redis running. I have a convenient shell script that uses Docker images:

    $ ./start-redis.sh

If you need to access the CLI, I have a script for that too:

    $ ./start-redis-cli.sh

### Setup Python

I used Python 3.8. Should work with any modern version. Regardless, make sure it is installed and then setup a virtual environment, activate it, and then upgrade pip so it doesn't nag you:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip

Install the requirements:

    $ pip install -r requirements.txt

### Setup anmd Invoke the Gear

I've got a couple of Python scripts for this as well. Setup, then invoke:

    $ python setup-gear.py
    $ python invoke-gear.py

If everything is correct, you should see:

    [b'65']
    [b'19']

That's it for now!
