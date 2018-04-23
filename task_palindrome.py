def is_palindrome(s):
        s = str (s)
        s = s.replace(' ', '')
        a = s[::-1]
        if s == a:
            print ('True')
            return s == a
        else:
            print ('False')
            return s == a

is_palindrome('Сел в озере березов лес')



