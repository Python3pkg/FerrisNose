Ferris Nose
===========

A nose plugin for bootstrapping the GAE SDK and GAE Testbed for Ferris.

Based on nose-gunit (https://github.com/beaulyddon-wf/nose-gunit)


Usage
-----

Run nosetests with the --with-ferris flag.

    nosetests --with-ferris app/tests

Note that this must be in the root of your project. If no path is provided the 'app/tests' is assumed.

If you get an error that it couldn't find the app engine sdk, then specify it using the --gae-sdk-path flag.

    nosetests --with-ferris --gae-sdk-path=/opt/gae app/tests

You can also set the APPENGINE_SDK_PATH environment variable.
