import numpy as np
import os
import matplotlib.pyplot as plt

def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum(((point - centroid)**2)))

def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)#find closest centroid
    return [index_of_minimum, data_point, centroids[index_of_minimum]]

def compute_new_centroids(data_points, centroids):
    return np.array(data_points + centroids)/2

def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    f = open("/Users/leslie/Downloads/Simple-k-Means-Clustering-Python-master/centroids.csv", 'w+')
    centroids_list = []
    
    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            for index_centroid in range(0, k):
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])  #label[1]:datapoint 
            print(centroids[label[0]])
            
     
                        
            if iteration == (total_iteration - 1):
                cluster_label.append(label)

    return [cluster_label, centroids,centroids_list]
def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))

def create_centroids():
    centroids = []
    centroids.append([5.0, 0.0])
    centroids.append([45.0, 70.0])
    centroids.append([50.0, 90.0])
    return np.array(centroids)



if __name__ == "__main__":
    filename = os.path.dirname(__file__) + "/data.csv"

    data_points = np.genfromtxt(filename, delimiter=",")

    centroids = create_centroids()
    total_iteration = 1
    
    [cluster_label, new_centroids,centroids_list] = iterate_k_means(data_points, centroids, total_iteration)


    print()
    print_label_data([cluster_label, new_centroids])
    print()

fig = plt.figure()
ax1 = fig.add_subplot(111)
for i in range(0,90):
    
    ax1.scatter(data_points[i,0],data_points[i,1],c = 'r',marker = 'o')
for i in range(0,3):
    ax1.scatter(new_centroids[i,0],new_centroids[i,1],c  = 'b',marker = 'v')




# =============================================================================
# ax2 = fig.add_subplot(111)
# for data in cluster_label:
#     if data[0]==0:
#         ax2.scatter(data[1,0],data[1,1],c='r')
#     if data[0]==1:
#         ax2.scatter(data[1,0],data[1,1],c='b')
#     if data[0]==2:
#         ax2.scatter(data[1,0],data[1,1],c='g')
#         
# =============================================================================

plt.xlim((5,120))
plt.ylim((5,150))
plt.show()


# =============================================================================
# rows_1 = np.random.randint(15,30, size=(25,2))
# rows_2 = np.random.randint(40,70, size=(25,2))
# rows_3 = np.random.randint(90,110, size=(25,2))
# 
# 
# data_points = np.row_stack((data_points,rows_1))
# data_points = np.row_stack((data_points,rows_2))
# data_points = np.row_stack((data_points,rows_3))
# 
# 
# np.savetxt('new.csv', data_points, delimiter = ',')
# =============================================================================















