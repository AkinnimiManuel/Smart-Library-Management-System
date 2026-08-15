

#Function to generate ID
def generate_Id(records, prefix, start):
    if not records: 
        return f"{prefix}{start:03d}"

    highest_id = max(int(record["id"][len(prefix):]) for record in records)

    return f"{prefix}{highest_id + 1:03d}"