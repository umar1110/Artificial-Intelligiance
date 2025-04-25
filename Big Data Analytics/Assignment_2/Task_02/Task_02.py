from collections import defaultdict

# Map Function
def mapper(line):
    month, rainfall = line.strip().split(',')
    return (month, float(rainfall)) 

# Reduce Function
def reducer(mapped_data):
    total_by_month = defaultdict(float)
    count_by_month = defaultdict(int)

    for month, rainfall in mapped_data:
        total_by_month[month] += rainfall
        count_by_month[month] += 1

    average_by_month = {
        month: total_by_month[month] / count_by_month[month]
        for month in total_by_month
    }
    return average_by_month

def main():
    file_path = "rainfall.txt"
    mapped_results = []

    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                mapped_results.append(mapper(line))

   
    reduced_results = reducer(mapped_results)

    
    for month, avg in reduced_results.items():
        print(f"{month}\t{avg:.1f}")

if __name__ == "__main__":
    main()
