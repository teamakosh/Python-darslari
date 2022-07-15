sonlar = list (range(1,11))
for son in sonlar:
    print(f'{son}ning kvadrati{son**2}ga teng')
    # 1ning kvadrati 1 ga teng
    # 2ning kvadrati 4 ga teng
    # 3ning kvadrati 9 ga teng
    # 4ning kvadrati 16 ga teng
    # 5ning kvadrati 25 ga teng
    # 6ning kvadrati 36 ga teng
    # 7ning kvadrati 49 ga teng
    # 8ning kvadrati 64 ga teng
    # 9ning kvadrati 81 ga teng
    # 10ning kvadrati 100 ga teng

sonlar=list(range(11))
sonlar_kvadrati=[]
for sonlar in sonlar:
     sonlar_kvadrati.append(son**2)
     print(sonlar)
     print(sonlar_kvadrati)
     
     #[0,   1,  2,  3,  4,  5,  6,  7,   8,  9,  10]
     # [ 0, 1,  4,  9,  16, 25, 36, 49,  64, 81, 100]  