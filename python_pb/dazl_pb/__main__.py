def get_argparse():
    from argparse import ArgumentParser
    parser = ArgumentParser('dazl_pb')
    subparsers = parser.add_subparsers(title='command', dest='command')
    subparsers.required = True
    subparsers.add_parser('fetch')
    subparsers.add_parser('grpc-gen')
    subparsers.add_parser('grpc-rewrite')
    return parser


def main(argv=None):
    parser = get_argparse()
    p = parser.parse_args()
    if p.command == 'fetch':
        from .fetch import fetch
        fetch()
    elif p.command == 'grpc-gen':
        from .grpc_gen import grpc_gen
        grpc_gen()
    elif p.command == 'grpc-rewrite':
        from .grpc_rewrite import grpc_rewrite
        grpc_rewrite()


main()
