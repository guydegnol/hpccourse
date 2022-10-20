from distutils.core import setup

setup(
    name='hpcgpu',
    version='0.0.1',
    author='GUillaume Therin',
    author_email='guillaume@therin.co',
    py_modules=['nvcc_plugin', 'v2.v2', 'v1.v1', 'common.helper', 'hpcourse.hpcourse'],
    url='https://github.com/guydegnol/hpcgpu_course',
    license='LICENSE',
    description='to run CUDA C/C++ code',
    #description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
