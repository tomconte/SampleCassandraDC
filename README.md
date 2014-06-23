SampleCassandraDC
=================

This is an example showing how to access a distributed Cassandra cluster from a Python app using Flask.

To run it you will need Python and some pre-reqs for the Cassandra driver:

```
apt-get install python-pip
apt-get install python-dev
apt-get install libev4 libev-dev
```

Then you can use pip to install the [DataStax Python driver](https://github.com/datastax/python-driver) for Cassandra and [Flask](http://flask.pocoo.org/):

```
pip install blist
pip install cassandra-driver
pip install Flask
```
