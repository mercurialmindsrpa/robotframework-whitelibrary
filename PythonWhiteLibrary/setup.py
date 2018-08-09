import distutils.sysconfig
from distutils.core import setup
from distutils.extension import Extension
setup(name         = 'robotframework-whitelibrary2',
      version      = '0.0.5',
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'SALabs',
      author_email = 'to.be.added@noexist89a887.org',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      packages     = ['WhiteLibrary'],
      package_dir  = {'WhiteLibrary' : ''},
      package_data = {'WhiteLibrary' : ['CSWhiteLibrary.dll']},
      )
