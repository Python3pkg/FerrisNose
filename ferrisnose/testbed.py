

class SimpleTestBed(object):
    """
    Creates a limited testbed, this is used before loading test
    files to fix issues with modules that touch google services before
    an http request. This also fixes the httplib2 library from being
    obtuse during tests.
    """
    def __init__(self):
        from google.appengine.ext import testbed
        self.testbed = testbed.Testbed()

    def activate(self):
        from google.appengine.datastore import datastore_stub_util
        self.testbed.activate()
        policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=1)
        self.testbed.init_datastore_v3_stub(consistency_policy=policy)
        self.testbed.init_urlfetch_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_logservice_stub()

    def deactivate(self):
        try:
            self.testbed.deactivate()
        except:
            pass
