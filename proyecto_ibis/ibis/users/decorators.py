from django.shortcuts import redirect

def testGuardian(function):
    def wrap(request,*args,**kwargs):
        if(request.user.is_staff):
            redirect('login')

        return(function(request,*args,**kwargs))
    return wrap