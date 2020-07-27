import time
import asyncio
# Generators
def odds(start,stop):
    for i in range(start,stop+1,2):
        yield(i)



async def count_num():
    print("one")
    await asyncio.sleep(1)
    print("two")


async def main():
    await asyncio.gather(count_num(),count_num(),count_num())

if __name__ == "__main__":
    asyncio.run( main())

# g = odds(1,15)
# print (next (g))
# print(next(g))
# print(tuple(g))