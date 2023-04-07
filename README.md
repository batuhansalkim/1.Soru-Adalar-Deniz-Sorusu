# 1.Soru-Adalar-Deniz-Sorusu
1.Soru Adalar Deniz Sorusu

////********LEETCODE ÜZERİNDEN PYTHON3 FORMATINDA ÇÖZÜM YAPILDI LEETCODE UYGUN DUYARLI SEO UYUMLU YAPMAYA ÇALIŞTIM*********//////

s (kara) ve s (su) haritasını temsil eden bir m x n2B ikili ızgara verildiğinde, adaların sayısını döndürüyor .grid'1''0'

Bir ada su ile çevrilidir ve bitişik karaların yatay veya dikey olarak bağlanmasıyla oluşur. Izgaranın dört kenarının da suyla çevrili olduğunu varsayalım

 Örnek:
Girdi: ızgara = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Çıkış: 3

Kısıtlamalar:

* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 300
* grid[i][j]veya . '0'_'1'

Burada Breadth-First Search (BFS) geçişini kullanabiliriz ve her BFS geçiş çağrısından sonra, o ana kadar bulunan ada sayısını artırabiliriz .
BFS'yi matris hücrelerinin her birinde, ancak ve ancak o öğe/hücre zaten ziyaret edilmemişse yapacağız. Şimdi, o elemanın/hücrenin ziyaret edilip edilmediğine karar vermek için şöyle yaklaştım olaya

Yaklaşım: Bu durumda orijinal hücre değerini değiştireceğiz. Değeri "1" ise toprak olduğunu ve değeri "0" ise su olduğunu biliyoruz. Yani bir hücreyi ziyaret ettikten sonra, değeri “1” den “0” a veya “-1” gibi herhangi bir değeri değiştirerek ziyaret edildiğini işaretleyebiliriz. Bu, o hücredeki değer "1" ise BFS'yi çalıştıracağımız için çalışacaktır. 

BFS aramasının başlangıcında, mevcut hücre çiftini ziyaret edilen kümeye ekleyebiliriz.
Sırasıyla bir liste kullanarak bu hücrenin sol, sağ, üst ve alt komşularını şu şekilde ekleyiyorum:[[0,-1], [0,1],[-1,0],[1,0]]
Burada ilk eleman row_idve ikincisi, column_id eklemek istediğimiz her komşu için current row id vecurrent col id
Aşağıdaki durumlarda belirli bir komşuyu ziyaret edecek: -
Satır dizini değerleri sınırlar içinde
Sütun dizini değerleri sınırlar içinde
Komşuda depolanan dize değeri == '1'
Hücre zaten ziyaret edilmedi
Bu 4 koşul aşağıda gösterilmiştir:

if 0 <= (col+col_id) < num_cols and 0 <= (row+row_id ) < num_rows and grid[row+row_id][col+col_id] == “1” and (row+row_id,col+col_id) not in visited

Bu koşullar aşağıda gösterildiği gibi karşılanırsa, bu tür her bir hücrede BFS'yi arasın
findIsland(row+row_id,col+col_id)

Her BFS çağrısı döndükten sonra, sayımı artırıyor.
Henüz ziyaret edilmemişse, sonraki hücrede BFS'yi araayaak
Son olarak, bulunan adaların sayısını döndürcek ve kod tamamlanmış oluyor
