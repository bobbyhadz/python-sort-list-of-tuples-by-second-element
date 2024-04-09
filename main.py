# Sort a list of tuples by the second element in Python

# ✅ sort a list of tuples by second element (ascending order)
list_of_tuples = [(1, 50), (1, 20),  (1, 30)]

sorted_list = sorted(
    list_of_tuples,
    key=lambda t: t[1]
)

print(sorted_list)  # 👉️ [(1, 20), (1, 30), (1, 50)]