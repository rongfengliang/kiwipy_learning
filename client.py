import kiwipy

with kiwipy.connect('amqp://dalong:dalong123@127.0.0.1/') as comm:
    # Send an RPC message
    response = comm.rpc_send('fib', 30).result()
    print((" [.] Got %r" % response))
    datas = [1,2]
    response = comm.rpc_send('msg', msg={"name":"dalong"}).result()
    print((" [.] Got %r" % response))
    response = comm.rpc_send('msgv2', msg={"name":"dalong"}).result()
    print((" [.] Got %r" % response))