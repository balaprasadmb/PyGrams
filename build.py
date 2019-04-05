from __future__ import print_function
import argparse
import jenkinsapi
import time

__version__ = '0.1.0'


def main():
    """ parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description='A Jenkins job trigger.')
    parser.add_argument('-V', '--version', dest='version', action='store_true', help="show version")
    parser.add_argument('--host', help="Specify Jenkins host")
    parser.add_argument('--username', help="Specify Jenkins auth username")
    parser.add_argument('--password', help="Specify Jenkins auth password")
    parser.add_argument('--job-name', help="Specify Jenkins job name to be triggered")
    parser.add_argument('--url', help="Specify url")
    parser.add_argument('--suites', help="Specify suites.")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    if not (args.host and args.username and args.password):
        print("Remote Jenkins auth info missing.")
        exit(1)

    if not args.job_name:
        print("Remote Jenkins job name not specified.")
        exit(1)

    return trigger(args)


def trigger(args):
    """ trigger remote Jenkins to build job.
    """
    jenkins_client = jenkinsapi.jenkins.Jenkins(
        args.host,
        username=args.username,
        password=args.password
#         'http://localhost:8080',
#         username='bborade',
#         password='Me@1812$'
    )
    print("> > > > initializing remote job {0} on node {1} and executing suites {2}.".format(args.job_name, args.url, args.suites))
    params = {
        "url": args.url,
        "suites": args.suites
    }
    job = jenkins_client[args.job_name]
    queue_item = job.invoke(build_params=params)

    print("> > > > Remote Jenkins job invoked, block until build complete.")
    while True:
        if queue_item.is_running():
            print('Broke')
            break
    build = queue_item.get_build()
    print(build.is_running())
    c_old = ""
    while build.is_running():
        console = build.get_console()
        new = console.replace(c_old, '')
        if new != "":
            print(new)
        c_old = console
        time.sleep(1)
    queue_item.block_until_complete()
    build = queue_item.get_build()
    build_status = build.get_status()
    build_number = build.get_number()
    print("> > > > Remote Jenkins job #{0} finished, build status: {1}.".format(
        build_number, build_status))
    return 0 if build_status == "SUCCESS" else 1


if __name__ == '__main__':
    main()