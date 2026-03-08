#  [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
#  [Red,Red,Blue,Blue]

import math

def EuDistance(P1,P2):
    EuclideanDist = math.sqrt((P1["X"]-P2["X"]) ** 2 + (P1["Y"]-P2["Y"]) ** 2)
    return EuclideanDist

def KNearestNeighbourClassifier():
    
    data = [
        {'Point':'A','X':1,'Y':2,'Label':'Red'},
        {'Point':'B','X':2,'Y':3,'Label':'Red'},
        {'Point':'C','X':3,'Y':1,'Label':'Blue'},
        {'Point':'D','X':6,'Y':5,'Label':'Blue'},
        {'Point':'E','X':5,'Y':3,'Label':'Blue'}
    ]

    x = int(input("Enter X coordinate:"))
    y = int(input("Enter Y coordinate:"))

    for i in data:
        print(i)

    new_points = {'X':x,'Y':y}

    for d in data:
        d['distance'] = EuDistance(d,new_points)
    
    print("Calculated distances are:")
    
    for d in data:
        print(d)

    sorted_data = sorted(data, key = lambda item : item['distance'])
    print("Sorted data is:",sorted_data)

    for d in sorted_data:
        print(d)

    k = 5
    #k = 5
    nearest = sorted_data[:k]
    
    print("Nearest 5 elements are:")
    
    for d in nearest:
        print(d)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['Label']
        votes[label] = votes.get(label,0) + 1

    print("Voting Result:")
    
    for d in votes:
        print("Name:",d, "Number of votes:",votes[d])

    predicted_class = max(votes, key=votes.get)

    print("Predicted class of", x,y ,"is:",predicted_class)

def main():
    KNearestNeighbourClassifier()

if __name__ =='__main__':
    main()



