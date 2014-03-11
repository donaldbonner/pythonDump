from multiprocessing import Process

def f(name):
    print 'hello', name
def g(name):
	print 'goodbye', name

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()