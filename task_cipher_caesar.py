def encode(text,rot = 0):
        coded_text = []
        for i in text:
                if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                        if 65 <= ord(i) <= 90 and ord(i) + rot > 90:
                                 coded_text = coded_text + list(chr((ord(i) - 26) + rot))
                        elif 97 <= ord(i) <= 122 and ord(i) + rot > 122:
                                                 coded_text = coded_text + list(chr((ord(i) - 26) + rot))
                        else:
                                 coded_text = coded_text + list(chr(ord(i) + rot))
                else:
                        coded_text = coded_text + [i]
        coded_text = ''.join(coded_text)
        print (coded_text)
        return coded_text

encode(Hello, Python3!,1)
                       
        

def decode(text,rot = 0):
        decoded_text = []
        for i in text:
                if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                        if 65 <= ord(i) <= 90 and ord(i) - rot < 65:
                                 decoded_text = decoded_text + list(chr((ord(i) + 26) - rot))
                        elif 97 <= ord(i) <= 122 and ord(i) - rot < 97:
                                                 decoded_text = decoded_text + list(chr((ord(i) + 26) - rot))
                        else:
                                 decoded_text = decoded_text + list(chr(ord(i) - rot))
                else:
                        decoded_text = decoded_text + [i]
        decoded_text = ''.join(decoded_text)
        print (decoded_text)
        return decoded_text

decode("Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg.",13)
