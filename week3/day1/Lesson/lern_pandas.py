import pandas as pd
data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)

print(df.head())    # Use head() to view the first few rows of the DataFrame.
print(df.describe())    # Use describe() to get a statistical summary of the numerical columns.
print(df.info())    # Use info() to get a concise summary of the DataFrame, including the number of non-null entries in each column.
print(df.sort_values(by='Price'))    # Sort the DataFrame based on the Price or Copies Sold.
print(df[df['Price'] > 9])    # Filter the books by a specific Genre or books with Price above a certain threshold.
print(df.groupby('Author').sum("Copies Sold"))    # Group the books by Author and sum up the Copies Sold.
