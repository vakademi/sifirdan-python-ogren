# Arguments Nedir?
# args


def args_function(*args):
    print(args)
    for item in args:
        print(item)
    print()
    print(args[3])


args_function('hakan', 2, 4, 'ercan', 1000, )


# Keyword Arguments Nedir?
# kwargs

def keyargs_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name'])


keyargs_function(name='hakan', password='1234')


def args_with_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


def args_with_kwargs__(*ttt, **ddd):
    print(ttt)
    print(ddd)


args_with_kwargs(1, 2, 3, 4, name='hakan', password='1234')
args_with_kwargs__(1, 2, 3, 4, name='hakan', password='1234')
