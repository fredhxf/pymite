#  -*- coding: utf-8 -*-
#  File: utils.py
""" utils module. """


__author__ = 'Otto Hockel <hockel.otto@googlemail.com>'
__docformat__ = 'plaintext'


from functools import wraps


def declassify(to_remove, *args, **kwargs):
    """ flatten the return values of the mite api.
    """
    def argdecorate(fn):
        """ enable the to_remove argument to the decorator. """
        # wrap the function to get the original docstring
        @wraps(fn)
        def declassed(*args, **kwargs):
            # call the method
            ret = fn(*args, **kwargs)
            try:
                # ensure that ret is a list
                if type(ret) is list:
                    return [r[to_remove] for r in ret]
                return ret[to_remove]
            except KeyError:
                # except errors that are thrown by the api
                return ret
        return declassed
    return argdecorate

# vim: set ft=python ts=4 sw=4 expandtab :
