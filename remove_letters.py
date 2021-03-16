#remove initial letters from K
test_list = ['czlowiek', 'Arkansas', 'Kuba', 'Kaka']

print(f"Oryginalna lista: {str(test_list)}")

#initializing K
K = 3
#map & lambda
# remove front k elements in str list
resoults = list(map(lambda i: i [K :], test_list))

print(f"Lista bez liter {K} od K: {str(resoults)}")