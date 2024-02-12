from faker import Faker
import pandas as pd
import random

# Set different localization
fake = Faker(['en_US',])
# Set a seed for reproducibility
Faker.seed(4321)

def generate_synthetic_data(num_samples):
    data_1 = {fake.text(): 0 for _ in range(num_samples // 2)}

    data_2 = []
    for _ in range(num_samples // 2):
        # Ensure at least one personal record in the text
        personal_data = [random.choice([fake.name(), fake.address(), fake.ssn(), str(fake.date_of_birth()), fake.ascii_email(), fake.phone_number()])]

        # Add up to 5 more personal records
        for _ in range(random.randint(0, 5)):
            personal_data.append(random.choice([fake.name(), fake.address(), fake.ssn(), str(fake.date_of_birth()), fake.ascii_email(), fake.phone_number(), fake.text()]))

        data_2.append((' '.join(personal_data), 1))

    # Combine dictionaries
    combined_data = dict(data_1 | dict(data_2))

    # Convert to DataFrame
    df = pd.DataFrame(combined_data.items(), columns=['text', 'has_personal_data'])

    # Shuffle the DataFrame
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return df