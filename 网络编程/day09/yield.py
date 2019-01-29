


def fun():
    print("启动生成器")
    yield 1 
    print("完成生成器")

f = fun()

print(next(f))
print(next(f))

(19637, 'zoo', 'n. (also fml  zoological gardens) place (eg a garden, park, etc) where living (esp wild) animals are kept for exhibition, study and breeding')
