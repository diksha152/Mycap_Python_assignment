from typing import List
 
def printChar(string: str) -> None:
    # Initializing array of List type
    arr: List[List[str]] = [[] for _ in range(len(string) + 1)]
 
    freq = [0] * 256
    # Maping frequency map
    for i in range(len(string)):
        freq[ord(string[i])] += 1
 
    # Traversing frequency array
    for i in range(256):
        if freq[i] > 0:
            # If frequency array is greater than zero
            # then storing its character on
            # i-th(frequency of that character) index
            # of arr
            arr[freq[i]].insert(0, chr(i))
 
    # Traversing arr from backwards as we need greater
    # frequency character first
    for i in range(len(arr) - 1, -1, -1):
        if arr[i]:
            for ch in arr[i]:
                print(f"{ch}-{i}")
 
# Driver Code
if __name__ == "__main__":
    str = "mississippi"
    printChar(str)
