#make list of fav places
fav_places = ['Manila, Philippines', 'Paris, France','Seoul, South Korea', 'Tokyo, Japan', 'Bangkok, Thailand']
#print original list
print("Original list: ", fav_places)

# sort list alphabetically using sorted() without changing list
print("Sorted list: ",sorted(fav_places))

# sort list reverse alphabetical order using sorted() without changing list
print("Reverse sorted list: ",sorted(fav_places, reverse=True))

#sort list using reverse() to reverse the original order
reverse_list = fav_places.reverse()
print(" Reverse list: ",fav_places)

#sort list using reverse() to reverse the reversed order
list_reverse = fav_places.reverse()
print("Reversed reverse list: ", fav_places)
#sort list with sort() to alphabetical order
sort_list = fav_places.sort()
print("Sort list: ", fav_places)
#sort list with sort() to reverse alphabetical order
list_sort = fav_places.sort(reverse=True)
print("Sort reverse list: ", fav_places)

