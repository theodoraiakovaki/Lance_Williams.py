import sys

method=sys.argv[1]
filename = sys.argv[2]
with open(filename, 'r') as f:
    line = f.readline().strip()
    numbers = [int(num) for num in line.split()]
numbers.sort()
clusters = [[num] for num in numbers]
#finding distance for each cluster and adding them to the dist list
dist =[]
for i in range(len(clusters)):
    for j in range(i+1,len(clusters)):
        distance= abs(clusters[i][0] - clusters[j][0])
        dist.append((distance, clusters[i], clusters[j]))

def merging_clusters(clusters, dist, method):
    d_uv=0
    while len(clusters) > 1: 
         #finding minimum distance between clusters and creating a new cluster
         min_distance, c1, c2 = min(dist)
         new_cluster= c1+c2
         new_cluster.sort()
         clusters.append(new_cluster)
         clusters.remove(c1)
         clusters.remove(c2)
         new_dist = [] 
         for c in clusters:
            if (c!=new_cluster):
             if method== single:
              d_uv=  0.5 * euclidian_distance(c1,c,dist) + 0.5 * euclidian_distance(c2,c,dist) - 0.5 *abs(euclidian_distance(c1,c,dist)-euclidian_distance(c2,c,dist))
             elif (method == complete):
                d_uv=  0.5 * euclidian_distance(c1,c,dist) + 0.5 * euclidian_distance(c2,c,dist) + 0.5 *abs(euclidian_distance(c1,c,dist)-euclidian_distance(c2,c,dist))
             elif (method == average):
                 d_uv= (len(c1)/(len(c1)+len(c2))) * euclidian_distance(c1,c,dist) + (len(c2)/(len(c1)+len(c2)))*euclidian_distance(c2,c,dist)
             elif (method == ward):
                 a1 = (len(c) + len(c1)) / (len(c) + len(c1) +len(c2))
                 a2 = (len(c) + len(c2)) / (len(c) + len(c1) +len(c2))
                 b= (len(c) / (len(c) + len(c1) +len(c2)))
                 d_uv = a1 * euclidian_distance(c1,c,dist) + a2 * euclidian_distance(c2,c,dist) - b * euclidian_distance(c1,c2,dist)
             #adding to the dist list the new distance between the new cluster and the others.
             new_dist.append((d_uv,new_cluster,c))
         #keeping all clusters except those containing c1 and c2 seperately 
         dist = [d for d in dist if d[1] not in [c1, c2]  not in [c1, c2] and d[2] not in [c1, c2]]
         dist = dist + new_dist
         if (c1<c2): 
            #print firstly cluster1 that is being merged with cluster2 
            print ("(" + " ".join(str(i) for i in c1) + ")", 
           "(" + " ".join(str(i) for i in c2) + ")", format(min_distance,'.2f'), len(new_cluster))
         else:
            print ("(" + " ".join(str(i) for i in c2) + ")", 
           "(" + " ".join(str(i) for i in c1) + ")", format(min_distance,'.2f'), len(new_cluster))


#finding the distance between x (cluster1) and y (cluster2) in the dist list.
def euclidian_distance(x,y,dist):
    for d in dist:
        if x in (d[1], d[2]) and y in (d[1], d[2]):
          distance_x_y = d[0]
    return distance_x_y
        
        
def single(clusters,dist):
    merging_clusters(clusters,dist, single)

def complete(clusters,dist):
   merging_clusters(clusters, dist, complete)

def average(clusters,dist):
    merging_clusters(clusters, dist, average)

def ward(clusters,dist):
    merging_clusters(clusters, dist, ward)


if method == 'complete':
   complete(clusters,dist)
elif method == 'single':
    single(clusters,dist)
elif method == 'average':
    average(clusters,dist)
elif method == 'ward':
    ward(clusters,dist)


