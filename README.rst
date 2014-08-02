mwtemplates
==================

.. image:: http://img.shields.io/travis/danmichaelo/mwtemplates.svg?style=flat
   :target: https://travis-ci.org/danmichaelo/mwtemplates
   :alt: Build status

.. image:: http://img.shields.io/coveralls/danmichaelo/mwtemplates.svg
   :target: https://coveralls.io/r/danmichaelo/mwtemplates
   :alt: Test coverage

.. image:: https://pypip.in/version/mwtemplates/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/mwtemplates/
   :alt: Latest Version

.. image:: https://pypip.in/py_versions/mwtemplates/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/mwtemplates/
   :alt: Supported Python versions

.. image:: https://pypip.in/download/mwtemplates/badge.svg?period=month&style=flat
   :target: https://pypi.python.org/pypi/mwtemplates/
   :alt: Downloads

mwtemplates is a simple wikitext template parser and editor, based on a python rewrite of the mediawiki preprocessorDOM.php. Tested with python 2.6, 2.7, 3.2 and 3.3.

It can be installed directly off github:

.. code-block:: console

    $ pip install git+git://github.com/danmichaelo/mwtemplates.git

(There is also a version on PyPi that can be installed using ``pip install mwtemplates`` or ``easy_install mwtemplates``)

Running tests
-------------------

To run tests, clone the repo and do:

.. code-block:: console
    
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt
    $ py.test -x tests --pep8 mwtemplates -v --cov mwtemplates --doctest-modules

Usage examples
-------------------

Edit a template:

.. code-block:: python

    from mwtemplates import TemplateEditor
    txt = u"""
    {{Infoboks geografi
    | kart = Svalbard_kart1.png
    | land = Norge
    | status = Øygruppe
    | administrasjon = [[Odd Olsen Ingerø]] ''<small>(2009)</small>''
    | administrasjonsnavn = [[Sysselmannen på Svalbard|Sysselmann]]
    | areal = 61022
    | befolkning = 2527
    | befolkningsår = [[2011]]
    | url = www.sysselmannen.svalbard.no
    }}
    """
    te = TemplateEditor(txt)
    te.templates['infoboks geografi'][0].parameters['land'] = 'Russland'
    print te.wikitext()

Remove a template argument:

.. code-block:: python

    from mwtemplates import TemplateEditor
    te = TemplateEditor(u"Hello {{mytpl | a=2 | b=3 | c=4 }} world")
    te.templates['mytpl'].parameters.remove('b')

Remove the first instance of a template:

.. code-block:: python

    from mwtemplates import TemplateEditor
    te = TemplateEditor(u"Hello {{mytpl}} world {{mytpl}}")
    te.templates['mytpl'][0].remove()
