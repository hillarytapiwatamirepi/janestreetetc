#!/usr/bin/python

# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function

import sys
import socket
import json
# from datetime import date
import datetime as dt
from time import sleep


bids = {}
offers ={}





# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name="firenation"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = False

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index=0
prod_exchange_hostname="production"

port=25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

# ~~~~~============== NETWORKING CODE ==============~~~~~
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile('rw', 1)

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def read_from_exchange(exchange):
    return json.loads(exchange.readline())


# ~~~~~============== MAIN LOOP ==============~~~~~

def main():
    exchange = connect()
    write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})
    # hello_from_exchange = read_from_exchange(exchange)
    # A common mistake people make is to call write_to_exchange() > 1
    # time for every read_from_exchange() response.
    # Since many write messages generate marketdata, this will cause an
    # exponential explosion in pending messages. Please, don't do that!
    # print(hello_from_exchange)
    # def buying_and_selling_order_every_ten_minute():
    #     id = 0 
    #     t = dt.datetime.now()
    #     while True:
    #         delta = dt.datetime.now()-t
    #         if delta.seconds >= 5:
    #             bids[id] = {"type": "add", "order_id": id, "symbol": "BOND", "dir": "BUY", "price":999, "size": 20}
    #             offers[id] = {"type": "add", "order_id": id, "symbol": "BOND", "dir": "SELL", "price":1001, "size": 20}
    #             write_to_exchange(exchange, {"type": "add", "order_id": id, "symbol": "BOND", "dir": "BUY", "price":999, "size": 20})
               
    #             # print(message)
    #             write_to_exchange(exchange,{"type": "add", "order_id": id, "symbol": "BOND", "dir": "SELL", "price":1001, "size": 20})

    #             message = read_from_exchange(exchange)
                # message = read_from_exchange(exchange)
                # print(message)


    # buying_and_selling_order_every_ten_minute()
    id = 1
    # bids[id] = {"type": "add", "order_id": id, "symbol": "BOND", "dir": "BUY", "price":999, "size": 20}
    # offers[id] = {"type": "add", "order_id": id, "symbol": "BOND", "dir": "SELL", "price":1001, "size": 20}
    write_to_exchange(exchange, {"type": "add", "order_id": id, "symbol": "BOND", "dir": "BUY", "price":999, "size": 20})
    id = 2
    write_to_exchange(exchange,{"type": "add", "order_id": id, "symbol": "BOND", "dir": "SELL", "price":1001, "size": 20})
    print(read_from_exchange(exchange))
    # print("The exchange replied:", hello_from_exchange, file=sys.stderr)




if __name__ == "__main__":
    main()
