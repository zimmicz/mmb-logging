import setuptools

setuptools.setup(name='mmb_logging',
      version='0.3',
      description='mapmybook logging',
      url='http://github.com/zimmicz/map-my-book-logging',
      author='Michal Zimmermann',
      author_email='zimmi@tutanota.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['sentry_sdk', 'sentry_sdk[flask]'],
      zip_safe=False)

