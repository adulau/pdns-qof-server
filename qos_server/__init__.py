#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A pdns-qof compliant passive DNS interface for the pdns-toolkit
#
# https://github.com/adulau/pdns-qof-server/
# https://github.com/adulau/pdns-toolkit/
#
# The pdns-qof - Passive DNS Query Output Format Description are described at
#
# https://github.com/adulau/pdns-qof
#
# Software is free software released under the "Modified BSD license"
#
# Copyright (c) 2013 Alexandre Dulaunoy - a@foo.be

import tornado.escape
from tornado.ioloop import IOLoop
import tornado.web
import tornado.process
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

import argparse
import sys
import signal

from .query import Query


def handle_signal(sig, frame):
    IOLoop.instance().add_callback(IOLoop.instance().stop)


class InfoHandler(tornado.web.RequestHandler):
    def get(self):
        response = {'version': 'git',
                    'software': 'pdns-qof-server'}
        self.write(response)


class QueryHandler(tornado.web.RequestHandler):

    # Default value in Python 3.5
    # https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
    nb_threads = tornado.process.cpu_count() * 5
    executor = ThreadPoolExecutor(nb_threads)

    @run_on_executor
    def run_request(self, q):
        to_return = []
        if query.is_ip(q):
            for x in query.getAssociatedRecords(q):
                to_return.append(query.getRecord(x))
        else:
            to_return.append(query.getRecord(t=q.strip()))
        return to_return

    @tornado.gen.coroutine
    def get(self, q):
        print("query: " + q)
        try:
            responses = yield self.run_request(q)
            for r in responses:
                self.write(r)
        except Exception as e:
            print('Something went wrong with {}:\n{}'.format(q, e))
        finally:
            self.finish()


class FullQueryHandler(tornado.web.RequestHandler):
    # Default value in Python 3.5
    # https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
    nb_threads = tornado.process.cpu_count() * 5
    executor = ThreadPoolExecutor(nb_threads)

    @run_on_executor
    def run_request(self, q):
        to_return = []
        if query.is_ip(q):
            for x in query.getAssociatedRecords(q):
                to_return.append(query.getRecord(x))
        else:
            for x in query.getAssociatedRecords(q):
                to_return.append(query.getRecord(t=x.strip()))
        return to_return

    @tornado.gen.coroutine
    def get(self, q):
        print("fquery: " + q)
        try:
            responses = yield self.run_request(q)
            for r in responses:
                self.write(r)
        except Exception as e:
            print('Something went wrong with {}:\n{}'.format(q, e))
        finally:
            self.finish()


def main():
    global query
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    argParser = argparse.ArgumentParser(description='qof-server server')
    argParser.add_argument('-o', default='https://www.circl.lu/pdns/', help='Origin of the PDNS (default: https://www.circl.lu/pdns/)')
    argParser.add_argument('-p', default=8888, help='qof-server TCP port (default 8888)')
    argParser.add_argument('-l', default='localhost', help='qof-server listen address (default localhost)')
    argParser.add_argument('-rp', default=6379, help='redis-server TCP port (default 8888)')
    argParser.add_argument('-rl', default='localhost', help='redis-server listen address (default localhost)')
    argParser.add_argument('-rd', default=0, help='redis-server database (default 0)')
    args = argParser.parse_args()
    origin = args.o
    port = args.p
    listen = args.l
    redis_port = args.rp
    redis_listen = args.rl
    redis_db = args.rd

    query = Query(redis_listen, redis_port, redis_db, origin)

    application = tornado.web.Application([
        (r"/query/(.*)", QueryHandler),
        (r"/fquery/(.*)", FullQueryHandler),
        (r"/info", InfoHandler)
    ])

    application.listen(port, address=listen)
    IOLoop.instance().start()
    IOLoop.instance().stop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
elif __name__ == "test":
    query = Query('localhost', 6379, 0, 'https://www.circl.lu/pdns/')
    qq = ["foo.be", "8.8.8.8"]

    for q in qq:
        if query.is_ip(q):
            for x in query.getAssociatedRecords(q):
                print(query.getRecord(x))
        else:
                print(query.getRecord(t=q))
