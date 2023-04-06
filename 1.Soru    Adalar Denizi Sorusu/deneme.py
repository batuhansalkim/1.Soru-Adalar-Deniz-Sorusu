#Batuhan Salkım#
#1210505904#

from typing import List;
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows,num_cols,num_islands = len(grid), len(grid[0]),0
        visited = set()
        
        def findIsland(row,col):
            # bu hücreyi ziyaret edilen kümeye ekle
            visited.add((row,col))
            
            # sırasıyla bu hücrenin sol, sağ, üst ve alt komşularını topla
            #Burada ilk eleman satır kimliği ve ikincisi sütun kimliğidir.
            neighbours = [[0,-1], [0,1],[-1,0],[1,0]]
            
            for row_id,col_id in neighbours:
                # İndeks değerleri sınırlar içindeyse ve string değeri neighbour == "1: konumunda saklanıyorsa ve
                # bu hücre zaten ziyaret edilmemişse, belirli bir komşuyu ziyaret et
                if 0 <= (col+col_id) < num_cols and 0 <= (row+row_id ) < num_rows and grid[row+row_id][col+col_id] == "1" and (row+row_id,col+col_id) not in visited:
                    findIsland(row+row_id,col+col_id)

        for row in range(num_rows):
            for col in range(num_cols):
                # zaten ziyaret edilmemişse her hücre öğesini çağır

                if grid[row][col] == "1" and (row,col) not in visited:
                    findIsland(row,col)
                    
                    # indIsland() yürütmesini döndürdüyse sayımı artırın
                    # çünkü bu, bir dizi sürekli hücrenin geçildiği anlamına gelir
                    num_islands += 1
        return num_islands