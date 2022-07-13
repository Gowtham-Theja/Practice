
s="{{[]}"
s1='[(){}]'
def balbrac(st):
    out = []
    l=[]
    l[:]=st

    for i in l:
        if i in '({[':
            out.append(i)
        else:
            curr_char = out.pop()
            if curr_char=='(':
                if i!=')':
                    return False
            if curr_char=='{':
                if i!='}':
                    return False
            if curr_char=='[':
                if i!=']':
                    return False
    if out:
        return False
    return True

def balbrac1(st):
    for i in range(len(st)-1):
        for y in ['()','[]','{}']:
            if y in ['[]','{}','()']:
                st.replace(y,'')
    return st