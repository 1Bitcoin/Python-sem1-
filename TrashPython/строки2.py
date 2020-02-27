srt = input('input string: ')

print(' '.join(srt.split()))
nsrt = srt.split()
i = 1
print(nsrt)
for z in nsrt:
    print(z)
    if z.istitle():
        nsrt = nsrt[:i] + nsrt[i+1:]
        i += 1
    i += 1
print(nsrt)

            



