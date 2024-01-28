import sys

def analyze_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        intruding_cats = 0
        total_time_in_house = 0
        visit_lengths = []

        for line in lines:
            if line.strip() == 'END':
                break
            
            # Extract cat, entry time, and exit time from each line.

            cat, entry_time, exit_time = line.strip().split(',')
            entry_time = int(entry_time)
            exit_time = int(exit_time)

            # Analyze cat visits and other cats in the log.

            if cat == 'OURS':
                cat_visits += 1
                total_time_in_house += exit_time - entry_time
                visit_lengths.append(exit_time - entry_time)
            elif cat == 'THEIRS':
                intruding_cats += 1

        if cat_visits > 0:
            avg_visit_length = sum(visit_lengths) // len(visit_lengths)
            longest_visit = max(visit_lengths)
            shortest_visit = min(visit_lengths)

            print("\nLog File Analysis")
            print("==================\n")
            print(f"Cat Visits: {cat_visits}")
            print(f"Other Cats: {intruding_cats}\n")
            print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n")
            print(f"Average Visit Length: {avg_visit_length // 60} Hours, {avg_visit_length % 60} Minutes")
            print(f"Longest Visit:        {longest_visit // 60} Hours, {longest_visit % 60} Minutes")
            print(f"Shortest Visit:       {shortest_visit // 60} Hours, {shortest_visit % 60} Minutes")
        else:

             # Inform if no visits by the correct cat are found in the log.

            print("No visits by the correct cat found in the log.")

    except FileNotFoundError:
                # Handle the case where the specified log file is not found.

        print(f'Cannot open "{file_path}"!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        analyze_log_file(sys.argv[1])