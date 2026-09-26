# Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
# Practice Problem: Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).

scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} 
threshold = 75

ans = dict()
for i in scores:
    if scores[i]>threshold:
        ans[i]=scores[i]
print("Passing Students : ",ans)

# 2.4