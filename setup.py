import setuptools

setuptools.setup(name='mmb_logger',
      version='0.1',
      description='mapmybook logger',
      url='http://github.com/zimmicz/map-my-book-logger',
      author='Michal Zimmermann',
      author_email='zimmi@tutanota.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['sentry_sdk', 'sentry_sdk.integrations.flask'],
      zip_safe=False)

