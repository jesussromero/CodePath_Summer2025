def nana(x):
    nanana = ''
    batman = 'batman!'

    if x <= 0: return print(batman)

    for i in range(x):
        nanana += 'na'

    nanana = nanana + ' ' + batman
    print(nanana)

if __name__ == "__main__":
    nana(-1)
    nana(0)
    nana(3)