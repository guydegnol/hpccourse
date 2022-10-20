from distutils.core import setup


def get_version():
    for filename in [f"{get_parameter()}/{f}" for f in ["__version__.py", "__init__.py"]]:
        if os.path.exists(filename):
            for line in read(filename).splitlines():
                if line.startswith("__version__"):
                    delim = '"' if '"' in line else "'"
                    return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


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
