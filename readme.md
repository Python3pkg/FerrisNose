Ferris Nose
===========

A nose plugin for testing Google App Engine applications. Built for the [Ferris Framework](http://ferrisframework.org) but can be used for testing any app engine application.

Originally based on [nose-gunit](https://github.com/beaulyddon-wf/nose-gunit).

Installation
------------

Install the latest version via pip:

    (sudo) pip install --upgrade ferrinose

Oh, Really?

Running Tests
-------------

Run nosetests with the --with-ferris flag.

    nosetests --with-ferris app/tests

Note that this must be in the root of your project. If no path is provided the 'app/tests' is assumed.

If you get an error that it couldn't find the app engine sdk, then specify it using the --gae-sdk-path flag.

    nosetests --with-ferris --gae-sdk-path=/opt/gae app/tests

You can also set the APPENGINE_SDK_PATH environment variable.


Writing Tests
-------------

For Ferris apps, see the [testing documentation](http://ferris-framework.appspot.com/docs/users_guide/testing.html).

For non-Ferris apps, create your test cases and inherit from ``ferrisnose.AppEngineTest``:

    from ferrisnose import AppEngineTest

    class TestPosts(AppEngineTest):
        def test_creation(self):
            post = Post(title="Hello!")
            post.put()

            assert Post.query().count() == 1

You can log-in users using the ``self.login_user(email, admin=False)`` and run deferred tasks using ``self.run_deferred_tasks(queue='default'``.

Additionally, there is a ``AppEngineWebTest`` class that provides a [webtest](http://webtest.pythonpaste.org/en/latest/index.html) instance at ``self.testapp``.
