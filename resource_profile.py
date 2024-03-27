'''
Created on 28-Sep-2023

@author: bborade
'''
import resource

dir(resource)
'''['RLIMIT_AS', 'RLIMIT_CORE', 'RLIMIT_CPU', 'RLIMIT_DATA', 'RLIMIT_FSIZE', 'RLIMIT_MEMLOCK', 'RLIMIT_MSGQUEUE', 'RLIMIT_NICE', 'RLIMIT_NOFILE', 'RLIMIT_NPROC', 'RLIMIT_OFILE', 'RLIMIT_RSS', 'RLIMIT_RTPRIO', 'RLIMIT_RTTIME', 'RLIMIT_SIGPENDING', 'RLIMIT_STACK', 'RLIM_INFINITY', 'RUSAGE_CHILDREN', 'RUSAGE_SELF', 'RUSAGE_THREAD', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'error', 'getpagesize', 'getrlimit', 'getrusage', 'prlimit', 'setrlimit', 'struct_rusage']'''

print(resource.getrlimit(resource.RLIMIT_CPU))

print(resource.getrusage(resource.RLIMIT_CPU))


