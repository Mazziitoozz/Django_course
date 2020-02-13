from django import template 

register = template.Library()

def cut(value,arg):
    '''
    This cuts out all values of "arg" from the string!
    '''
    return value.replace(arg,'')

register.filter('cut1',cut) #first argument it is the name which you are gonna register in template library and you are gonna use when you call,
                           # second argument it is the name of the function you want to register