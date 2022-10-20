from distutils.core import setup

setup(
    name='hpcgpu',
    version='0.1.5',
    author='Guillaume Therin',
    author_email='guillaume@therin.co',
    py_modules=['nvcc_plugin', 'v2.v2', 'v1.v1', 'common.helper', 'hpcourse.hpcourse', 'hpcourse.hpcourse3'],
    url='https://github.com/guydegnol/hpcgpu_course',
    license='LICENSE',
    description='Course on HPC with CUDA',
    #description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
