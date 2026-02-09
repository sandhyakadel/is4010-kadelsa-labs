# Lab 04 AI Prompts

## Problem 1: Finding Common Items

**Prompt:** I have two very large lists of product IDs and need to find which IDs appear in both lists. Performance is important, and the order of the result does not matter. What Python data structure should I use and why?

**Recommendation:** You should use a Set to solve this problem because it is the most efficient way to handle intersections between large collections of data. While comparing two lists directly is slow because Python has to scan every item repeatedly, sets use a process called hashing to find matches almost instantly. By converting your lists into sets and using the intersection operator, you reduce the workload from a nested search to a linear operation, which significantly improves performance. Since your requirements mention that the final order doesn't matter, the unordered nature of a set is a perfect fit for this scenario.

## Problem 2: User Profile Lookup

**Prompt:** I have a list of user profile dictionaries. I need to look up a user's full profile using their unique username. Because this lookup happens frequently and performance is critical, what data structure should I use to store these records, and why?

**Recommendation:** For high-performance lookups, you should use a Dictionary where the usernames serve as the keys and the profile objects serve as the values. While searching through a standard list requires Python to check every single entry until it finds a match, a dictionary uses a hash table to jump directly to the correct data. This changes your search time from linear complexity to constant time, meaning the lookup will stay lightning-fast regardless of whether you have ten users or ten million. This is the standard "caching" pattern used in professional software to handle frequent data retrieval.

## Problem 3: Listing Even Numbers in Order

**Prompt:** I need to filter even numbers from a list of integers while preserving the original order. What data structure or approach should I use?

**Recommendation:** You should use a List combined with a list comprehension to solve this. Since your primary requirement is to maintain the sequence of the sensor readings, a list is the ideal structure because it is ordered by nature. Using a list comprehension is the most efficient and "Pythonic" approach here; it allows you to iterate through the data, check if each number is even using the modulo operator, and build a new ordered list in a single, highly optimized step. This keeps your code concise and readable while ensuring the data remains in its original chronological order.