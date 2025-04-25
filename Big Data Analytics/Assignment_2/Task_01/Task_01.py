from collections import defaultdict


# Map Function
def mapper(line):
    product, amount = line.strip().split(',')
    return (product, int(amount))

# Reduce Function
def reducer(mapped_data):
    reduced_data = defaultdict(int)
    for product, amount in mapped_data:
        reduced_data[product] += amount
    return reduced_data


# Main Execution

def main():
    file_path = "sales.txt"
    mapped_results = []

  
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                mapped_results.append(mapper(line))

   
    reduced_results = reducer(mapped_results)

    # Output the final result
    for product, total in reduced_results.items():
        print(f"{product}\t{total}")

if __name__ == "__main__":
    main()
