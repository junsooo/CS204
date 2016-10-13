#20150606 JunSooLee
#CS204 HW8_PA
#Reference:
#https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
#Sorry for terrible reference

file = open("input.txt", "r");
# read integers from input text file
file2 = open("output.txt","w");
# write integers to output text file


vnum,enum,st,ed = [int(x) for x in file.readline().split()]
graph = [[0]*vnum for _ in range(vnum)]

for line in file:
    u, v, weight = [int(x) for x in line.split()]
    graph[u][v] = weight
    graph[v][u] = weight
#save edges information as a adjcency matrix

#### Your dijkstra algorithm will be HERE##########

#Should we consider the direction?? ->Ask to TA nim

#List of visited, unvisited nodes
visited=[]
unvisited=[]
for i in range(vnum):
	unvisited.append(i)

#To find the path after the dijkstra algorithm
path=[]
for i in range(vnum):
	path.append(vnum+1)

#To use after the dijkstra algorithm(Because st is changed on algorithm)
st_real=st
ed_real=ed
#Initiate the list of distance
inf=2100000000	#huge const.
dist = []
for i in range(st):
	dist.append(inf)
dist.append(0)
for i in range(vnum-st-1):
	dist.append(inf)

#Now, we know the starting point's index. Start dijkstra algorithm
#While there is no unvisited node

#When start!=end!!!
if st_real!=ed_real:
	while len(unvisited)>0:
		#Next, Go to next node from starting point(node)
		for i in range(vnum):
			if graph[st][i]!=0:	#Connected next node
				if dist[st]+graph[st][i]<dist[i]:	#Change dist[i] to minimum value
					dist[i]=dist[st]+graph[st][i]
					path[i]=st 		#Trace the path!
		#Mark starting point as 'visited'
		visited.append(st)
		unvisited.remove(st)

		#Now we find the next minimum distance node
		min_check=inf+1
		for v_idx in unvisited:
			if min_check>dist[v_idx]:
				min_check=dist[v_idx]

		#Change st as next min_dist node!
		for v_idx in unvisited:
			if dist[v_idx]==min_check:
				st=v_idx
				break
###############################################
#Algorithm finished
if st_real!=ed_real:
	if dist[ed]==inf:
		file2.write("There is no path from source to destination.")
	else:
		result = "%d %d %d\n" % (st_real, ed, dist[ed])
		file2.write(result)
else:
	file2.write("Start node equals End node.")
#How about Start node = End node? ->Ask to TA nim

#To find out the path to go end node
path_list=[]
path_list.append(ed)

#Get the path_list, with reversed order
if dist[ed]!=inf:
	while ed!=st_real:
		path_list.append(path[ed])
		ed=path[ed]

path_list.reverse()


for i in range(len(path_list)-1):
	path = "%d %d %d\n" % (path_list[i],path_list[i+1],graph[path_list[i]][path_list[i+1]])
	file2.write(path)
