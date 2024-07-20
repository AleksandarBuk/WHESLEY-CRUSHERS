# animals_info.py

def create_animals_list():
    return [
    {"id": 1, "name": "Rex", "weight": 30, "age": 5, "species": "Cow", "breed": "Holstein"},
    {"id": 2, "name": "Buddy", "weight": 15, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 3, "name": "Ivan", "weight": 20, "age": 12, "species": "Dog", "breed": "Rottweiler"},
    {"id": 4, "name": "Read", "weight": 9, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 5, "name": "Ivan", "weight": 7, "age": 13, "species": "Cat", "color": "Orange"},
    {"id": 6, "name": "Red", "weight": 12, "age": 9, "species": "Cat", "color": "Yellow"},
    {"id": 7, "name": "Gri", "weight": 32, "age": 10, "species": "Dog", "breed": "Shepard"},
    {"id": 8, "name": "Max", "weight": 25, "age": 6, "species": "Dog", "breed": "Labrador"},
    {"id": 9, "name": "Bella", "weight": 8, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 10, "name": "Lucy", "weight": 11, "age": 8, "species": "Cat", "color": "White"},
    {"id": 11, "name": "Jack", "weight": 18, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 12, "name": "Molly", "weight": 7, "age": 2, "species": "Cat", "color": "Brown"},
    {"id": 13, "name": "Charlie", "weight": 28, "age": 4, "species": "Cow", "breed": "Holstein"},
    {"id": 14, "name": "Luna", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 15, "name": "Cooper", "weight": 22, "age": 9, "species": "Dog", "breed": "Bulldog"},
    {"id": 16, "name": "Daisy", "weight": 12, "age": 7, "species": "Cat", "color": "Calico"},
    {"id": 17, "name": "Bailey", "weight": 24, "age": 11, "species": "Dog", "breed": "Poodle"},
    {"id": 18, "name": "Simba", "weight": 14, "age": 4, "species": "Cat", "color": "Orange"},
    {"id": 19, "name": "Riley", "weight": 19, "age": 8, "species": "Dog", "breed": "Yorkshire Terrier"},
    {"id": 20, "name": "Nala", "weight": 6, "age": 1, "species": "Cat", "color": "White"},
    {"id": 21, "name": "Oscar", "weight": 33, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 22, "name": "Sophie", "weight": 8, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 23, "name": "Ziggy", "weight": 27, "age": 9, "species": "Dog", "breed": "Dachshund"},
    {"id": 24, "name": "Ginger", "weight": 9, "age": 3, "species": "Cat", "color": "Red"},
    {"id": 25, "name": "Murphy", "weight": 20, "age": 5, "species": "Dog", "breed": "Cocker Spaniel"},
    {"id": 26, "name": "Mittens", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 27, "name": "Rocco", "weight": 29, "age": 8, "species": "Dog", "breed": "Great Dane"},
    {"id": 28, "name": "Whiskers", "weight": 7, "age": 4, "species": "Cat", "color": "Brown"},
    {"id": 29, "name": "Rexy", "weight": 21, "age": 5, "species": "Dog", "breed": "Australian Shepherd"},
    {"id": 30, "name": "Toby", "weight": 16, "age": 7, "species": "Dog", "breed": "Schnauzer"},
    {"id": 31, "name": "Tigger", "weight": 13, "age": 9, "species": "Cat", "color": "Orange"},
    {"id": 32, "name": "Chloe", "weight": 5, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 33, "name": "Sam", "weight": 31, "age": 6, "species": "Dog", "breed": "Pug"},
    {"id": 34, "name": "Felix", "weight": 11, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 35, "name": "Rocky", "weight": 26, "age": 10, "species": "Dog", "breed": "Bulldog"},
    {"id": 36, "name": "Maggie", "weight": 15, "age": 8, "species": "Cat", "color": "White"},
    {"id": 37, "name": "Jasper", "weight": 23, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 38, "name": "Peanut", "weight": 6, "age": 3, "species": "Cat", "color": "Brown"},
    {"id": 39, "name": "Buster", "weight": 18, "age": 7, "species": "Dog", "breed": "Labrador"},
    {"id": 40, "name": "Paws", "weight": 12, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 41, "name": "Rufus", "weight": 25, "age": 9, "species": "Dog", "breed": "Hound"},
    {"id": 42, "name": "Lily", "weight": 9, "age": 5, "species": "Cat", "color": "Calico"},
    {"id": 51, "name": "Rex", "weight": 30, "age": 5, "species": "Dog", "breed": "Husky"},
    {"id": 52, "name": "Buddy", "weight": 15, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 53, "name": "Ivan", "weight": 20, "age": 12, "species": "Dog", "breed": "Rottweiler"},
    {"id": 54, "name": "Read", "weight": 9, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 55, "name": "Ivan", "weight": 7, "age": 13, "species": "Cat", "color": "Orange"},
    {"id": 56, "name": "Red", "weight": 12, "age": 9, "species": "Cat", "color": "Yellow"},
    {"id": 57, "name": "Gri", "weight": 32, "age": 10, "species": "Dog", "breed": "Shepard"},
    {"id": 58, "name": "Max", "weight": 25, "age": 6, "species": "Dog", "breed": "Labrador"},
    {"id": 59, "name": "Bella", "weight": 8, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 60, "name": "Lucy", "weight": 11, "age": 8, "species": "Cat", "color": "White"},
    {"id": 61, "name": "Jack", "weight": 18, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 62, "name": "Molly", "weight": 7, "age": 2, "species": "Cat", "color": "Brown"},
    {"id": 63, "name": "Charlie", "weight": 28, "age": 4, "species": "Dog", "breed": "Golden Retriever"},
    {"id": 64, "name": "Luna", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 65, "name": "Cooper", "weight": 22, "age": 9, "species": "Dog", "breed": "Bulldog"},
    {"id": 66, "name": "Daisy", "weight": 12, "age": 7, "species": "Cat", "color": "Calico"},
    {"id": 67, "name": "Bailey", "weight": 24, "age": 11, "species": "Dog", "breed": "Poodle"},
    {"id": 68, "name": "Simba", "weight": 14, "age": 4, "species": "Cat", "color": "Orange"},
    {"id": 69, "name": "Riley", "weight": 19, "age": 8, "species": "Dog", "breed": "Yorkshire Terrier"},
    {"id": 70, "name": "Nala", "weight": 6, "age": 1, "species": "Cat", "color": "White"},
    {"id": 71, "name": "Oscar", "weight": 33, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 72, "name": "Sophie", "weight": 8, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 73, "name": "Ziggy", "weight": 27, "age": 9, "species": "Dog", "breed": "Dachshund"},
    {"id": 74, "name": "Ginger", "weight": 9, "age": 3, "species": "Cat", "color": "Red"},
    {"id": 75, "name": "Murphy", "weight": 20, "age": 5, "species": "Dog", "breed": "Cocker Spaniel"},
    {"id": 76, "name": "Mittens", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 77, "name": "Rocco", "weight": 29, "age": 8, "species": "Dog", "breed": "Great Dane"},
    {"id": 78, "name": "Whiskers", "weight": 7, "age": 4, "species": "Cat", "color": "Brown"},
    {"id": 79, "name": "Rexy", "weight": 21, "age": 5, "species": "Dog", "breed": "Australian Shepherd"},
    {"id": 80, "name": "Toby", "weight": 16, "age": 7, "species": "Dog", "breed": "Schnauzer"},
    {"id": 81, "name": "Tigger", "weight": 13, "age": 9, "species": "Cat", "color": "Orange"},
    {"id": 82, "name": "Chloe", "weight": 5, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 83, "name": "Sam", "weight": 31, "age": 6, "species": "Dog", "breed": "Pug"},
    {"id": 84, "name": "Felix", "weight": 11, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 85, "name": "Rocky", "weight": 26, "age": 10, "species": "Dog", "breed": "Bulldog"},
    {"id": 86, "name": "Maggie", "weight": 15, "age": 8, "species": "Cat", "color": "White"},
    {"id": 87, "name": "Jasper", "weight": 23, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 88, "name": "Peanut", "weight": 6, "age": 3, "species": "Cat", "color": "Brown"},
    {"id": 89, "name": "Buster", "weight": 18, "age": 7, "species": "Dog", "breed": "Labrador"},
    {"id": 90, "name": "Paws", "weight": 12, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 91, "name": "Rufus", "weight": 25, "age": 9, "species": "Dog", "breed": "Hound"},
    {"id": 92, "name": "Lily", "weight": 9, "age": 5, "species": "Cat", "color": "Calico"},
    {"id": 93, "name": "Baxter", "weight": 17, "age": 6, "species": "Dog", "breed": "Terrier"},
    {"id": 94, "name": "Lola", "weight": 13, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 95, "name": "Rocky", "weight": 28, "age": 8, "species": "Dog", "breed": "Collie"},
    {"id": 96, "name": "Mimi", "weight": 6, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 97, "name": "Duke", "weight": 34, "age": 9, "species": "Dog", "breed": "Mastiff"},
    {"id": 98, "name": "Pinky", "weight": 10, "age": 2, "species": "Cat", "color": "White"},
    {"id": 99, "name": "Ranger", "weight": 22, "age": 7, "species": "Dog", "breed": "Setter"},
    {"id": 100, "name": "Nina", "weight": 11, "age": 6, "species": "Cat", "color": "Orange"},
    {"id": 101, "name": "Rex", "weight": 30, "age": 5, "species": "Dog", "breed": "Husky"},
    {"id": 102, "name": "Buddy", "weight": 15, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 103, "name": "Ivan", "weight": 20, "age": 12, "species": "Dog", "breed": "Rottweiler"},
    {"id": 104, "name": "Read", "weight": 9, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 105, "name": "Ivan", "weight": 7, "age": 13, "species": "Cat", "color": "Orange"},
    {"id": 106, "name": "Red", "weight": 12, "age": 9, "species": "Cat", "color": "Yellow"},
    {"id": 107, "name": "Gri", "weight": 32, "age": 10, "species": "Dog", "breed": "Shepard"},
    {"id": 108, "name": "Max", "weight": 25, "age": 6, "species": "Dog", "breed": "Labrador"},
    {"id": 109, "name": "Bella", "weight": 8, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 110, "name": "Lucy", "weight": 11, "age": 8, "species": "Cat", "color": "White"},
    {"id": 111, "name": "Jack", "weight": 18, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 112, "name": "Molly", "weight": 7, "age": 2, "species": "Cat", "color": "Brown"},
    {"id": 113, "name": "Charlie", "weight": 28, "age": 4, "species": "Dog", "breed": "Golden Retriever"},
    {"id": 114, "name": "Luna", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 115, "name": "Cooper", "weight": 22, "age": 9, "species": "Dog", "breed": "Bulldog"},
    {"id": 116, "name": "Daisy", "weight": 12, "age": 7, "species": "Cat", "color": "Calico"},
    {"id": 117, "name": "Bailey", "weight": 24, "age": 11, "species": "Dog", "breed": "Poodle"},
    {"id": 118, "name": "Simba", "weight": 14, "age": 4, "species": "Cat", "color": "Orange"},
    {"id": 119, "name": "Riley", "weight": 19, "age": 8, "species": "Dog", "breed": "Yorkshire Terrier"},
    {"id": 120, "name": "Nala", "weight": 6, "age": 1, "species": "Cat", "color": "White"},
    {"id": 121, "name": "Oscar", "weight": 33, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 122, "name": "Sophie", "weight": 8, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 123, "name": "Ziggy", "weight": 27, "age": 9, "species": "Dog", "breed": "Dachshund"},
    {"id": 124, "name": "Ginger", "weight": 9, "age": 3, "species": "Cat", "color": "Red"},
    {"id": 125, "name": "Murphy", "weight": 20, "age": 5, "species": "Dog", "breed": "Cocker Spaniel"},
    {"id": 126, "name": "Mittens", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 127, "name": "Rocco", "weight": 29, "age": 8, "species": "Dog", "breed": "Great Dane"},
    {"id": 128, "name": "Whiskers", "weight": 7, "age": 4, "species": "Cat", "color": "Brown"},
    {"id": 129, "name": "Rexy", "weight": 21, "age": 5, "species": "Dog", "breed": "Australian Shepherd"},
    {"id": 130, "name": "Toby", "weight": 16, "age": 7, "species": "Dog", "breed": "Schnauzer"},
    {"id": 131, "name": "Tigger", "weight": 13, "age": 9, "species": "Cat", "color": "Orange"},
    {"id": 132, "name": "Chloe", "weight": 5, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 133, "name": "Sam", "weight": 31, "age": 6, "species": "Dog", "breed": "Pug"},
    {"id": 134, "name": "Felix", "weight": 11, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 135, "name": "Rocky", "weight": 26, "age": 10, "species": "Dog", "breed": "Bulldog"},
    {"id": 136, "name": "Maggie", "weight": 15, "age": 8, "species": "Cat", "color": "White"},
    {"id": 137, "name": "Jasper", "weight": 23, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 138, "name": "Peanut", "weight": 6, "age": 3, "species": "Cat", "color": "Brown"},
    {"id": 139, "name": "Buster", "weight": 18, "age": 7, "species": "Dog", "breed": "Labrador"},
    {"id": 140, "name": "Paws", "weight": 12, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 141, "name": "Rufus", "weight": 25, "age": 9, "species": "Dog", "breed": "Hound"},
    {"id": 142, "name": "Lily", "weight": 9, "age": 5, "species": "Cat", "color": "Calico"},
    {"id": 143, "name": "Bella", "weight": 12, "age": 2, "species": "Bird", "breed": "Parrot"},
    {"id": 144, "name": "Milo", "weight": 5, "age": 3, "species": "Bird", "breed": "Canary"},
    {"id": 145, "name": "Charlie", "weight": 3, "age": 1, "species": "Bird", "breed": "Finch"},
    {"id": 146, "name": "Daisy", "weight": 15, "age": 4, "species": "Cow", "breed": "Jersey"},
    {"id": 147, "name": "Bessie", "weight": 1200, "age": 7, "species": "Cow", "breed": "Holstein"},
    {"id": 148, "name": "Moo", "weight": 1100, "age": 6, "species": "Cow", "breed": "Angus"},
    {"id": 149, "name": "Cluck", "weight": 2, "age": 1, "species": "Chicken", "breed": "Leghorn"},
    {"id": 150, "name": "Henrietta", "weight": 2, "age": 2, "species": "Chicken", "breed": "Rhode Island Red"},
    {"id": 151, "name": "Rex", "weight": 30, "age": 5, "species": "Dog", "breed": "Husky"},
    {"id": 152, "name": "Buddy", "weight": 15, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 153, "name": "Ivan", "weight": 20, "age": 12, "species": "Dog", "breed": "Rottweiler"},
    {"id": 154, "name": "Read", "weight": 9, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 155, "name": "Ivan", "weight": 7, "age": 13, "species": "Cat", "color": "Orange"},
    {"id": 156, "name": "Red", "weight": 12, "age": 9, "species": "Cat", "color": "Yellow"},
    {"id": 157, "name": "Gri", "weight": 32, "age": 10, "species": "Dog", "breed": "Shepard"},
    {"id": 158, "name": "Max", "weight": 25, "age": 6, "species": "Dog", "breed": "Labrador"},
    {"id": 159, "name": "Bella", "weight": 8, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 160, "name": "Lucy", "weight": 11, "age": 8, "species": "Cat", "color": "White"},
    {"id": 161, "name": "Jack", "weight": 18, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 162, "name": "Molly", "weight": 7, "age": 2, "species": "Cat", "color": "Brown"},
    {"id": 163, "name": "Charlie", "weight": 28, "age": 4, "species": "Dog", "breed": "Golden Retriever"},
    {"id": 164, "name": "Luna", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 165, "name": "Cooper", "weight": 22, "age": 9, "species": "Dog", "breed": "Bulldog"},
    {"id": 166, "name": "Daisy", "weight": 12, "age": 7, "species": "Cat", "color": "Calico"},
    {"id": 167, "name": "Bailey", "weight": 24, "age": 11, "species": "Dog", "breed": "Poodle"},
    {"id": 168, "name": "Simba", "weight": 14, "age": 4, "species": "Cat", "color": "Orange"},
    {"id": 169, "name": "Riley", "weight": 19, "age": 8, "species": "Dog", "breed": "Yorkshire Terrier"},
    {"id": 171, "name": "Oscar", "weight": 33, "age": 7, "species": "Dog", "breed": "Boxer"},
    {"id": 172, "name": "Sophie", "weight": 8, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 173, "name": "Ziggy", "weight": 27, "age": 9, "species": "Dog", "breed": "Dachshund"},
    {"id": 174, "name": "Ginger", "weight": 9, "age": 3, "species": "Cat", "color": "Red"},
    {"id": 175, "name": "Murphy", "weight": 20, "age": 5, "species": "Dog", "breed": "Cocker Spaniel"},
    {"id": 176, "name": "Mittens", "weight": 10, "age": 6, "species": "Cat", "color": "Black"},
    {"id": 177, "name": "Rocco", "weight": 29, "age": 8, "species": "Dog", "breed": "Great Dane"},
    {"id": 178, "name": "Whiskers", "weight": 7, "age": 4, "species": "Cat", "color": "Brown"},
    {"id": 179, "name": "Rexy", "weight": 21, "age": 5, "species": "Dog", "breed": "Australian Shepherd"},
    {"id": 180, "name": "Toby", "weight": 16, "age": 7, "species": "Dog", "breed": "Schnauzer"},
    {"id": 181, "name": "Tigger", "weight": 13, "age": 9, "species": "Cat", "color": "Orange"},
    {"id": 182, "name": "Chloe", "weight": 5, "age": 2, "species": "Cat", "color": "Gray"},
    {"id": 183, "name": "Sam", "weight": 31, "age": 6, "species": "Dog", "breed": "Pug"},
    {"id": 184, "name": "Felix", "weight": 11, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 185, "name": "Rocky", "weight": 26, "age": 10, "species": "Dog", "breed": "Bulldog"},
    {"id": 186, "name": "Maggie", "weight": 15, "age": 8, "species": "Cat", "color": "White"},
    {"id": 187, "name": "Jasper", "weight": 23, "age": 5, "species": "Dog", "breed": "Beagle"},
    {"id": 188, "name": "Peanut", "weight": 6, "age": 3, "species": "Cat", "color": "Brown"},
    {"id": 189, "name": "Buster", "weight": 18, "age": 7, "species": "Dog", "breed": "Labrador"},
    {"id": 190, "name": "Paws", "weight": 12, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 191, "name": "Rufus", "weight": 25, "age": 9, "species": "Dog", "breed": "Hound"},
    {"id": 192, "name": "Lily", "weight": 9, "age": 5, "species": "Cat", "color": "Calico"},
    {"id": 193, "name": "Baxter", "weight": 17, "age": 6, "species": "Dog", "breed": "Terrier"},
    {"id": 194, "name": "Lola", "weight": 13, "age": 4, "species": "Cat", "color": "Black"},
    {"id": 195, "name": "Rocky", "weight": 28, "age": 8, "species": "Dog", "breed": "Collie"},
    {"id": 196, "name": "Mimi", "weight": 6, "age": 3, "species": "Cat", "color": "Gray"},
    {"id": 197, "name": "Duke", "weight": 34, "age": 9, "species": "Dog", "breed": "Mastiff"},
    {"id": 198, "name": "Pinky", "weight": 10, "age": 2, "species": "Cat", "color": "White"},
    {"id": 199, "name": "Ranger", "weight": 22, "age": 7, "species": "Dog", "breed": "Setter"},
    {"id": 200, "name": "Nina", "weight": 11, "age": 6, "species": "Cat", "color": "Orange"},
    {"id": 201, "name": "Sunny", "weight": 0.5, "age": 1, "species": "Bird", "breed": "Cockatiel"},
    {"id": 202, "name": "Oliver", "weight": 0.8, "age": 2, "species": "Bird", "breed": "Budgerigar"},
    {"id": 203, "name": "Peach", "weight": 1, "age": 4, "species": "Bird", "breed": "Lovebird"},
    {"id": 204, "name": "Bella", "weight": 600, "age": 4, "species": "Cow", "breed": "Guernsey"},
    {"id": 205, "name": "Maggie", "weight": 1300, "age": 9, "species": "Cow", "breed": "Jersey"},
    {"id": 206, "name": "Lily", "weight": 1500, "age": 7, "species": "Cow", "breed": "Holstein"},
    {"id": 207, "name": "Charlie", "weight": 2.5, "age": 1, "species": "Chicken", "breed": "Leghorn"},
    {"id": 208, "name": "Poppy", "weight": 2.8, "age": 2, "species": "Chicken", "breed": "Rhode Island Red"},
    {"id": 209, "name": "Ginger", "weight": 3, "age": 3, "species": "Chicken", "breed": "Plymouth Rock"},
    {"id": 210, "name": "Max", "weight": 8, "age": 5, "species": "Monkey", "breed": "Capuchin"},
    {"id": 211, "name": "Lola", "weight": 6, "age": 4, "species": "Monkey", "breed": "Marmoset"},
    {"id": 212, "name": "Bongo", "weight": 12, "age": 7, "species": "Monkey", "breed": "Squirrel Monkey"},
    {"id": 213, "name": "Ruby", "weight": 0.3, "age": 2, "species": "Bird", "breed": "Finch"},
    {"id": 214, "name": "Charlie", "weight": 1.2, "age": 5, "species": "Bird", "breed": "Parrot"},
    {"id": 215, "name": "Sunny", "weight": 0.9, "age": 3, "species": "Bird", "breed": "Canary"},
    {"id": 216, "name": "Sammy", "weight": 8, "age": 6, "species": "Monkey", "breed": "Spider Monkey"},
    {"id": 217, "name": "Nina", "weight": 0.7, "age": 1, "species": "Bird", "breed": "Budgerigar"},
    {"id": 218, "name": "Toby", "weight": 1.5, "age": 3, "species": "Bird", "breed": "Cockatiel"},
    {"id": 219, "name": "Bella", "weight": 1.4, "age": 6, "species": "Bird", "breed": "Lovebird"},
    {"id": 220, "name": "Rex", "weight": 12, "age": 8, "species": "Monkey", "breed": "Rhesus Monkey"}
]