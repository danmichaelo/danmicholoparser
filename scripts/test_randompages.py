# encoding=utf-8
from __future__ import unicode_literals
import mwclient
import logging
from mwtemplates import TemplateEditor

# "Note: This test requires internet connectivity!"

site = mwclient.Site('no.wikipedia.org')

logger = logging.getLogger()  # root logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('templateeditor-randompages-test.log', mode='w', encoding='utf-8')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# fc = logging.StreamHandler()
# fc.setFormatter(formatter)
# fc.setLevel(logging.INFO)
# logger.addHandler(fc)


# @with_setup(setup)
def test_randompages():
    n = 20
    # logger.info('Testing %d random pages. This may take some time.', n)
    pages = site.random(namespace=0, limit=n)
    for page in pages:
        logger.info('Testing page: %s', page['title'])
        yield check_randompage, page['title']


def check_randompage(pagename):
    logger.debug('Page: %s', pagename)
    page = site.pages[pagename]
    inputtxt = page.edit(readonly=True)
    dp = TemplateEditor(inputtxt)
    outputtxt = dp.wikitext()

    assert inputtxt == outputtxt
