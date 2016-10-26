from google.appengine.ext import ndb


class Transaction(ndb.Model):

    created = ndb.DateTimeProperty(auto_now_add=True)