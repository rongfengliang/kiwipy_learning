import threading
import kiwipy

def fib(comm, num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fib(comm, num - 1) + fib(comm, num - 2)

def msg(comm,datas):
    print("add",comm,datas)
    return dict(datas)

def msgv2(comm,*args,**kwargs):
    print("add",comm,args,kwargs)
    return dict(args, **kwargs)
     
with kiwipy.connect('amqp://dalong:dalong123@127.0.0.1/') as comm:
    # Register an RPC subscriber with the name 'fib'
    comm.add_rpc_subscriber(fib, 'fib')
    comm.add_rpc_subscriber(msg, 'msg')
    comm.add_rpc_subscriber(msgv2, 'msgv2')
    # Now wait indefinitely for fibonacci calls
    threading.Event().wait()