# lst = [1,2,3]
# my_str = 'mlops playlist'
# my_int = 123
# print(type(lst))

from opps_proj import chatbook

# user1 = chatbook()
# print(user1.get_name())

# user1.set_name("Agent X")
# print(user1.get_name())

# lst = [1,2,3]
# # function
# list_len = len(lst)
# print(list_len)

# # method
# user1 = chatbook()
# user1.send_msg()

# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)