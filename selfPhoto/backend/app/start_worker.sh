#!/bin/sh

# export PYTHONPATH="../../:$PYTHONPATH"


# python huey_consumer.py core.huey_app.huey -w2
#huey_consumer app.main.huey -w2
#huey_consumer.py -w 50 -k greenlet -C

huey_consumer app.main.huey -w 8