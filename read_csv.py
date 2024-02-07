import csv

def view_saved_face_data():
    filename = "/tmp/face_data.csv"

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        #Checking if there are rows in the csv
        try:
            header = next(reader) 
            print(header)
        except StopIteration:
            print("No data found in the CSV file.")
            return

        for row in reader:
            print(row)

if __name__ == "__main__":
    view_saved_face_data()
