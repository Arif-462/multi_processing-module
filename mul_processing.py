from multiprocessing import Pool

nums = [1,2,3,4,5,6]
def square(n):
    return n*n


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    
    with Pool() as p:
        result = p.map(square, nums)
    
    print(result)

