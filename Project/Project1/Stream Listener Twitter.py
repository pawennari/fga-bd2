# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:28:19 2019

@author: Alfian Alwi
"""

from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

consumer_key="JIZDcS8ryw0bLEwr0svo4e5Su"
consumer_secret="PyVZ0zYbMUqtxtC9MRw1N98NmZ54aBao2gne3NixDzmS2o6J40"
access_token="3258832214-d0V94yM7gOMLT4VXTKrvfassF2uSoctfT2zx0fR"
access_token_secret="ossefThWCqDPhsPorDte2zrFPJHXPfIKNN2UMDXZ5Uxb2"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['makan','nonton','tidur','main','boker'])