#ask uesr for items seperated by comma input = (a,b,c,d)
#convert that input into a list use split(",")
#use a loop to count every word in search use .lower().strip() 
#each duplicate words save how many there in a dic = {word1:number,word2:number}
#show the duplicate words and if not print that as a statement "No duplicates found."

def search_for_duplicates(items_list):
    duplicate = {}
    new_list = [item.lower().strip() for item in items_list]

    for item in new_list:
        if item in duplicate:
            continue
        count = new_list.count(item)
        if count > 1:
            duplicate[item] = count
    return duplicate

user_input = input("Enter a list of items seperated by a comma: ")
user_list = [x for x in user_input.split(",") if x.strip()]

dic = search_for_duplicates(user_list)
if not dic:
    print("No duplicates found.")
else:
    print("The duplicates found in the list:")
    for item,count in sorted(dic.items()):
        print(f"{item} x {count}")