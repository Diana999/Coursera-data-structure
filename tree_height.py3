import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        def fillDepth(self,  i , depth):
            if depth[i] != 0:
                return
            if self.parent[i] == -1:
                depth[i] = 1
                return
            if depth[self.parent[i]] == 0:
                self.fillDepth(self.parent[i] , depth)
            depth[i] = depth[self.parent[i]] + 1
        def findHeight(self):
            depth = [0]*self.n
            for i in range(self.n):
                self.fillDepth(i, depth)
            return max(depth)
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.findHeight())

threading.Thread(target=main).start()

