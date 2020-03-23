from  tkinter import *
def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    if src not in graph:
        raise TypeError('source not there in data')
    if dest not in graph:
        raise TypeError('destination not there data')    
    
    if src == dest:
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        readable=path[0]
        for index in range(1,len(path)):
            readable = path[index] + '--->' + readable
        p = Tk()
        p.title('Output')
        p['bg'] = 'black'
        Label(p,text=("path: " + readable + ",\tdistance=" + str(distances[dest])),fg='red',bg='black',font=('times', 18, 'italic bold')).grid(row=1)
        Label(p,text='THANK YOU!!!!!!',fg='green',bg='black',font=('times', 18, 'italic bold')).grid(row=2)
    else :
        if not visited: 
            distances[src]=0
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        visited.append(src)
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)
        

