from setuptools import setup, find_packages


requires = [
    'django',
    'django-debug-toolbar',
    'nose',
    'django-nose',
    'coverage',
    'django_coverage',
    'psycopg2',
    'django_extensions',
    'pillow',
    'django-bootstrap-pagination',
    'djorm-ext-pgfulltext',
    'six',
    'django-grappelli',
    'beautifulsoup4',
    'lxml',
]

setup(name='restorus',
      version='3.0',
      description='where authority and anarchy meet',
      author='Mark Tully',
      author_email='mark.tully@restorus.org',
      url='http://restorus.org',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )