def main():
    sep = raw_input()
    l=[]
    try:
        while True:
            c = raw_input()
            if c == '' or c=='\n':
                break
            else:
                l.append(c)
    except EOFError:
        pass
    except Exception:
        pass
    print sep.join(l)

main()
