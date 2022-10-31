def bomba(segundos):
    if(segundos==0):
        print('\n','KABOOM')
        return
    else:
        print('\n',segundos,'s...')
        bomba(segundos-1)
        

def main():
    bomba(5)
if __name__ == '__main__':
    main()