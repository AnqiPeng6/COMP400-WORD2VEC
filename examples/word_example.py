from gensim.models import KeyedVectors
import os

# Path to the GoogleNews-vectors-negative300.bin file in Downloads
model_path = os.path.expanduser("~/Downloads/GoogleNews-vectors-negative300.bin")

# Load the model (binary=True because it's in binary format)
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# Example usage
# Check if a word is in the vocabulary
word = "pretty"
if word in word2vec_model:
    print(f"'{word}' is in the vocabulary.")
else:
    print(f"'{word}' is not in the vocabulary.")

# Get the vector for a word
vector = word2vec_model[word]
print(f"Vector for '{word}':\n{vector}")

# Find the most similar words to a given word
similar_words = word2vec_model.most_similar("pretty", topn=5)
print("Top 5 words similar to 'pretty':")
for similar_word, similarity in similar_words:
    print(f"{similar_word}: {similarity}")

# Calculate similarity between two words
similarity = word2vec_model.similarity("pretty", "beautiful")
print(f"Similarity between 'pretty' and 'beautiful': {similarity}")
