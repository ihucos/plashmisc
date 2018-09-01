# plashmisc
An unstable macro library for plash

Example Usage:
```
$ plash run --from-ubuntu cosmic
plash: eval: macro 'from-ubuntu' not found
$ pip3 install  git+https://github.com/ihucos/plash.git
$ plash run --import plashmisc --from-ubuntu cosmic -- printf 'hi\n'
hi
```
