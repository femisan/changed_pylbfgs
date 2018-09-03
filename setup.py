from distutils.core import setup, Extension
import numpy.distutils.misc_util
import numpy

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

with open('VERSION', 'r') as f:
    version = f.read()

# include_dirs = ['/usr/local/include'].extend(numpy.distutils.misc_util.get_numpy_include_dirs())
# if include_dirs is None:
include_dirs = [numpy.get_include()]
include_dirs.append('/opt/local/include')

print (include_dirs)
ext_modules = [
    Extension(
        'pylbfgs',
        sources=['pylbfgs.c'],
        libraries=['lbfgs'],
        library_dirs=['/opt/local/lib'],
        include_dirs= include_dirs,
        runtime_library_dirs=['/opt/local/lib'],
        ),
    ]

setup(
    name='PyLBFGS',
    version=version,
    author='Robert Taylor',
    author_email='rtaylor@pyrunner.com',
    url='https://bitbucket.org/rtaylor/pylbfgs',
    description=(
        'PyLBFGS is a Python 3 wrapper of the libLBFGS '
        'library written by Naoaki Okazaki.'
        ),
    long_description=readme,
    license=license,
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        ],
    ext_modules=ext_modules,
)
