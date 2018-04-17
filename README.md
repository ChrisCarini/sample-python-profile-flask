# sample-python-profile-flask
A sample project to demonstrate profiling python flask web applications 


## Quick Start
To get started, simply:
1) **term 1:** `git clone git@github.com:ChrisCarini/sample-python-profile-flask.git`
2) **term 1:** `source setup.sh`
3) **term 1:** `python webapp.py runserver --debug`
4) **term 2:** `curl localhost:5000`
5) Kill the webapp started in step #3 (`[Cmd] + [C]` on OSX)
6) **term 1:** `snakeviz perf_test/GET.*.prof`
7) Browser should open, and you can view performance data in `snakeviz`  