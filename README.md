# mtg_toolkit
A series of scripts and data files to track and manage a magic the gathering collection.

Repo: [https://github.com/tempylionheart/mtg_toolkit/](https://github.com/tempylionheart/mtg_toolkit/)

This guide was written using bitbucket's markdown.
Tutorial: [https://bitbucket.org/tutorials/markdowndemo](https://bitbucket.org/tutorials/markdowndemo)

## Technology
This is built with:

* On Windows 10 (64-bit)
<!-- * Python 3.X is required to use versions of Django after 1.10 -->
* Python==3.4.3
* pip==7.1.2
<!-- * Amazon Linux 2016.09 v2.2.0 -->

<!--     [AWS Python Server Requirements](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html#concepts.platforms.python)
 -->
## Development Environment Setup
1. [Install Anaconda](https://www.continuum.io/downloads)

2. Run cmd as an administrator

3. Downgrade Anaconda python to sync with AWS version

        conda install python==3.4.3

4. Downgrade pip to sync with AWS server version

        easy_install pip==7.1.2

    pip will complain about needing an upgrade to version 9.X each time a package is installed. Ignore it.

<!-- ### Tutorial
[Deploying a Django Application to Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) -->

### Initial Setup for local Python

1. Setting up the virtual environment folder. Naming the folder "envConda343":

        pip install virtualenv
        virtualenv envConda343

2. Activating the virtual env

        \envConda343\Scripts\activate