# Minimum Öklid Mesafesinin Hesaplanması

# q2 + r-kare = p-kare
#karekök(x2-x1)-kare + (y2-y1)-kare) şeklinde hesaplanır. 

# Öklid mesafesi, Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. 
#Bu formül ile, düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabilirsiniz.

# Göreviniz

# Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

# Noktaların tanımlanması: 

#‘points’ adında bir liste oluşturun. 
#Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. 
#Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

#Öklid Mesafesi İçin Bir Fonksiyon Yazma:

#‘euclideanDistance’ adında bir fonksiyon tanımlayın.Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve 
#bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

#Mesafelerin Hesaplanması:

#Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. 
#Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

#Minimum Mesafenin Bulunması:

#‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.

##### KODLAR #####

# Öklid mesafesini hesaplayan fonksiyon

def euclideanDistance(x,y):
    # 2D görünüme sahip Her iki nokta arasındaki öklid mesafesinin hesabı: 
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    

#2D görünümlü noktaların listesi
points = [(1,2), (3,4), (5,6),(7,8), (9,10)]

#euclideanDistance fonksiyonundan dönen iki nokta arasındaki öklid mesafesini döndüren liste
distances = []

# points listesindeki her nokta çifti arasındaki mesafenin hesaplanması

for i in range(len(points)):
    for j in range(i+1, len(points)):# İç içe döngüde ikinci döngüdeki range'i i+1'den başlatmamın sebebi aynı nokta çiftini tekrar tekrar karşılaştırmamak
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# minimum mesafenin hesaplanması

min_distance = min(distances)
min_distance
