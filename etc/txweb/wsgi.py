
def application(env, response):
    '''
    Basic t.w.wsgi application
    '''
    response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello world!']
    
